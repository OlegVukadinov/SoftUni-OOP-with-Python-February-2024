from abc import ABC, abstractmethod
from typing import List


class BaseCampaign(ABC):
    unique_campaign_id = []

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers= []  # : List[BaseInfluencer]

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if not value >= 0:
            raise ValueError(f"Campaign ID must be a positive integer greater than zero.")
        if value in BaseCampaign.unique_campaign_id:
            raise ValueError(f"Campaign with ID {self.campaign_id} already exists. Campaign IDs must be unique.")
        else:
            BaseCampaign.unique_campaign_id.append(value)  # ili add(value)

        self.__campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass
