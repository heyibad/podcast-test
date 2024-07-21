import yaml
import xml.etree.ElementTree as xml_tree


with open("feed.yaml","r") as file:
    yaml_data= yaml.safe_load(file)

    rss_elemnt= xml_tree.Element("rss")

   
    'version':'2.0'
    'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content':'http://purl.org/rss/1.0/modules/content/'