from kwresearch.interfaces.keyword import Keyword, RelatedKeywords
from kwresearch.moz.mozapi import (Device, Engine, Location, akeyword_metrics,
                                   arelated_keywords, keyword_metrics,
                                   related_keywords)


class MozEngine:
    def __init__(
            self,
            device: Device = Device.DESKTOP,
            engine: Engine = Engine.GOOGLE,
            locale: Location = Location.US,
            max_related_keywords: int = 60
    ) -> None:
        self.device = device
        self.engine = engine
        self.locale = locale
        self.max_related_keywords = max_related_keywords

    def _get_related_keywords(self, keyword: str) -> RelatedKeywords:
        res = related_keywords(
            keyword=keyword,
            device=self.device,
            engine=self.engine,
            locale=self.locale,
            limit=self.max_related_keywords,
        )
        suggestions = [r["keyword"] for r in res["suggestions"]]
        rkws = []
        for suggestion in suggestions:
            metrics = keyword_metrics(
                keyword=suggestion,
                device=self.device,
                engine=self.engine,
                locale=self.locale,
            )["keyword_metrics"]
            volume = metrics["volume"]
            difficulty = metrics["difficulty"]
            organic_ctr = metrics["organic_ctr"]
            priority = metrics["priority"]
            rkws.append(Keyword(
                keyword=suggestion,
                volume=volume,
                difficulty=difficulty,
                organic_ctr=organic_ctr,
                priority=priority,
            ))
        return RelatedKeywords(
            keyword=keyword,
            location=self.locale,
            device=self.device,
            engine=self.engine,
            related_keywords=rkws,
        )
    
    def get_related_keywords(self, keyword: str) -> RelatedKeywords:
        return self._get_related_keywords(keyword)
    
    async def _aget_related_keywords(self, keyword: str) -> RelatedKeywords:
        res = await arelated_keywords(
            keyword=keyword,
            device=self.device,
            engine=self.engine,
            locale=self.locale,
            limit=self.max_related_keywords,
        )
        suggestions = [r["keyword"] for r in res["suggestions"]]
        rkws = []
        for suggestion in suggestions:
            metrics = await akeyword_metrics(
                keyword=suggestion,
                device=self.device,
                engine=self.engine,
                locale=self.locale,
            )
            volume = metrics["volume"]
            difficulty = metrics["difficulty"]
            organic_ctr = metrics["organic_ctr"]
            priority = metrics["priority"]
            rkws.append(Keyword(
                keyword=suggestion,
                volume=volume,
                difficulty=difficulty,
                organic_ctr=organic_ctr,
                priority=priority,
            ))
        return RelatedKeywords(
            keyword=keyword,
            location=self.locale,
            device=self.device,
            engine=self.engine,
            related_keywords=rkws,
        )
    
    async def aget_related_keywords(self, keyword: str) -> RelatedKeywords:
        return await self._aget_related_keywords(keyword)