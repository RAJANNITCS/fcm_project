from template_manager.models import CampaignTemplate
from advertiser.models import Campaign
import random


class CampaignTemplateView:
    def __init__(self, ad_type, total_div, *args,**kwargs):
        self.ad_type = ad_type
        self.total_div = total_div

    def details(self,):
        campaign = Campaign.objects.filter(active=True, ad_format=self.ad_type,)
        list_imageurl = []
        dict_imageurl = {}

        for i in range(int(self.total_div)):
            random_campaign = random.choice(campaign)
            url = random_campaign.template.final_url
            image = random_campaign.template.adimage
            dict_imageurl['image'] = str(image)
            dict_imageurl['url'] = str(url)
            list_imageurl.append(dict_imageurl)
        return list_imageurl