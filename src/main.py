from service import MqService
from settings import app_settings


mq_service = MqService(rabbit_url=app_settings.RABBITMQ_URI)


async def main():
    """
    Main function to run the application.
    Connects, sends RPC, prints response, and disconnects.
    """
    await mq_service.connect()
    try:
        response = await mq_service.send_rpc(
            target_queue=f"onlive-{app_settings.APP_ENV}-api-product-list",
            payload={
                "organizationId": "1babebad-3de0-4002-857d-eecaadd45482",
                "filter": {}
            },
            timeout=3
        )
        print(response)
    except TimeoutError as e:
        logger.error(f"RPC call timed out: {e}")
    except Exception as e:
        logger.error(f"An error occurred during RPC call: {e}", exc_info=True)
    finally:
        # Ensure connection is closed gracefully
        logger.info("Closing RabbitMQ connection...")
        await mq_service.stop()
        logger.info("RabbitMQ connection closed.")


if __name__ == "__main__":
    import asyncio
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application stopped by user.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
