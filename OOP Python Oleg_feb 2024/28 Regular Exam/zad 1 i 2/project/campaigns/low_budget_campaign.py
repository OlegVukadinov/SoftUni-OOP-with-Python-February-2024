from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    LOW_BUDGET_CAMPAIGN = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, LowBudgetCampaign.LOW_BUDGET_CAMPAIGN, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        if engagement_rate >= 90 * self.required_engagement / 100:  # Vnimanie ili samo 120
            return True
