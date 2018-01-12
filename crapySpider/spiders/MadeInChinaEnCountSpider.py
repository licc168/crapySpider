# -*- coding: utf-8 -*-
import scrapy,urllib,re
import re
'''
中国制造网英文版
'''

class MadeInChinaEnCountSpider(scrapy.Spider):
    name = "MadeInChinaEnCountSpider"
    countNum = 0
    #allowed_domains = ['login.made-in-china.com','made-in-china.com']
    start_urls = [
        # 化工数据统计
        # "http://www.made-in-china.com/manufacturers-directory/item3/Foam-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Plastic-Polymer-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Plastic-Products-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Rubber-Rubber-Products-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Paint-Coating-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Pigment-Dye-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Additive-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Chemical-Auxiliary-Catalyst-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Agricultural-Chemicals-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Fertilizer-1.html"
        #工业品
        # "http://www.made-in-china.com/manufacturers-directory/item3/Car-Light-Auto-Mirror-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Car-Accessories-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Fastener-Fitting-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Auto-Engine-Structure-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Auto-Parts-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Crank-Mechanism-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Abrasive-Grinding-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Diamond-Tools-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Drilling-Tools-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Hand-Tools-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Horticulture-Gardening-Products-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Power-Tools-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Building-Hardware-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Hardware-Accessories-1.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Machine-Hardware.html"


        # 产品-行业是10的
        # "http://www.made-in-china.com/Chemicals-Catalog/Foam.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Plastic-Polymer.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Plastic-Products.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Rubber-Rubber-Products.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Paint-Coating.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Pigment-Dye.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Organic-Chemicals.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Fiberglass-Products.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Inorganic-Chemicals.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Inorganic-Fiber.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Inorganic-Salt.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Additive.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Adhesive.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Artificial-Graphite-Active-Carbon.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Chemical-Auxiliary-Catalyst.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Chemical-Filling.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Chemical-Reagent.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Flux-Impregnant.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Specialized-Preparation.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Lubricant.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Petrochemical-Refining.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Wax-Fat.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Essential-Oil-Balsam-Fine-Chemicals.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Agricultural-Chemicals.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Fertilizer.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Rosin-Forest-Chemical.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Biochemical.html",
        # "http://www.made-in-china.com/Health-Medicine-Catalog/Pharmaceutical-Chemicals.html",
        # "http://www.made-in-china.com/Health-Medicine-Catalog/Pharmaceutical-Intermediate.html",
        # "http://www.made-in-china.com/Packaging-Printing-Catalog/Packaging-Materials.html",
        # "http://www.made-in-china.com/Packaging-Printing-Catalog/Printing-Materials.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Airbag.html",
        # "http://www.made-in-china.com/Manufacturing-Processing-Machinery-Catalog/Chemical-Equipment-Machinery.html",
        # "http://www.made-in-china.com/Light-Industry-Daily-Use-Catalog/Household-Plastic-Products.html",
        # "http://www.made-in-china.com/Manufacturing-Processing-Machinery-Catalog/Plastic-Machinery.html",
        # "http://www.made-in-china.com/Manufacturing-Processing-Machinery-Catalog/Rubber-Machinery.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Chemical-Waste.html",
        # "http://www.made-in-china.com/Instruments-Meters-Catalog/Lab-Supplies.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/New-type-Chemical-Material.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Photographic-Sensitive-Product.html",
        # "http://www.made-in-china.com/Chemicals-Catalog/Other-Chemicals.html"
         #产品行业是-8
        # "http://www.made-in-china.com/Auto-Parts-Accessories-Catalog/Car-Light-Auto-Mirror.html",
        # "http://www.made-in-china.com/Auto-Parts-Accessories-Catalog/Car-Accessories.html",
        # "http://www.made-in-china.com/Industrial-Equipment-Components-Catalog/Fastener-Fitting.html",
        # "http://www.made-in-china.com/Auto-Parts-Accessories-Catalog/Auto-Engine-Structure.html",
        # "http://www.made-in-china.com/Auto-Parts-Accessories-Catalog/Auto-Parts.html",
        # "http://www.made-in-china.com/Auto-Parts-Accessories-Catalog/Crank-Mechanism.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Abrasive-Grinding.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Diamond-Tools.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Drilling-Tools.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Hand-Tools.html",
        # "http://www.made-in-china.com/Light-Industry-Daily-Use-Catalog/Horticulture-Gardening-Products.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Hydraulic-Parts.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Power-Tools.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Building-Hardware.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Hardware-Accessories.html",
        # "http://www.made-in-china.com/Tools-Hardware-Catalog/Machine-Hardware.html"


        # 产品-行业3
        "http://www.made-in-china.com/Metallurgy-Mineral-Energy-Catalog/Alloy.html",
        "http://www.made-in-china.com/Metallurgy-Mineral-Energy-Catalog/Non-ferrous-Metal-Products.html",
        "http://www.made-in-china.com/Metallurgy-Mineral-Energy-Catalog/Steel-Products.html",
        "http://www.made-in-china.com/Metallurgy-Mineral-Energy-Catalog/Magnetic-Material.html",
        "http://www.made-in-china.com/Metallurgy-Mineral-Energy-Catalog/Solar-Renewable-Energy.html",
        "http://www.made-in-china.com/Metallurgy-Mineral-Energy-Catalog/Aluminum.html"


    ]

    def parse(self, response):
        max_pages_num = response.xpath('//div[@class="pager"]/div[@class="page-num"]/a[last()-1]/text()').extract()
        max_num = re.sub('\s','',max_pages_num[0])
        count = int(max_num)*30
        self.countNum = self.countNum+count
        print(count)
        print(self.countNum)

