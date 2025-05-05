from service import MqService
from settings import app_settings


mq_service = MqService(rabbit_url=app_settings.RABBITMQ_URI)


async def main():
    """
    Main function to run the application.
    """
    await mq_service.connect()
    response = await mq_service.send_rpc(
        target_queue=f"onlive-{app_settings.APP_ENV}-api-product-list",
        payload={
            "organizationId": "1babebad-3de0-4002-857d-eecaadd45482",
            "filter": {}
        }
    )

    print(response)


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
