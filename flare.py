import asyncio, upyog as upy

NAME = "flare"
LOG  = upy.get_logger(NAME)

async def main(**kwargs):
    LOG.info("Starting Up...")

if __name__ == "__main__":
    parser = upy.get_base_parser(NAME,
        description="Stellar Flares Analysis"                             
    )
    args   = parser.parse_args()

    asyncio.run(main(**vars(args)))