import enum
import logging

from kwresearch.moz import mozengine


class KWEngine(enum.Enum):
    MOZ = "moz"

class KWCloudBuilder:
    def __init__(
            self,
            keyword: str,
            depth: int = 2,
            kwengine: KWEngine = KWEngine.MOZ,
            device: mozengine.Device = mozengine.Device.DESKTOP,
            engine: mozengine.Engine = mozengine.Engine.GOOGLE,
            locale: mozengine.Location = mozengine.Location.US,
            verbose: bool = True
            ) -> None:
        assert kwengine == KWEngine.MOZ, "Only MOZ engine is supported at the moment"

        self.keyword = keyword
        if kwengine == KWEngine.MOZ:
            self.kwengine = mozengine.MozEngine(
                device=device,
                engine=engine,
                locale=locale
            )
        self.verbose = verbose

        if self.verbose:
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)
        else:
            logging.basicConfig(level=logging.ERROR)
            self.logger = logging.getLogger(__name__)

        self.cloud = {
            "keyword": self.keyword,
            "depth": depth,
            "device": device,
            "engine": engine,
            "locale": locale,
            "cloud": {}
        }

    def get_related_keywords(self):
        return self.kwengine.get_related_keywords(self.keyword)

    async def aget_related_keywords(self):
        return await self.kwengine.aget_related_keywords(self.keyword)
    
    # def _generate_cloud(self):
    #     for _depth in range(self.cloud["depth"]):
    #         if self.verbose:
    #             self.logger.info(f"Generating cloud for depth: {_depth}")
    #         related_keywords = self.