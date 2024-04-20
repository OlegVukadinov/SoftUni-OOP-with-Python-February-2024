from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.85

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)  # PremiumInfluencer.INITIAL_PAYMENT_PERCENTAGE

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * 0.85

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.5)
        elif campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.8)

