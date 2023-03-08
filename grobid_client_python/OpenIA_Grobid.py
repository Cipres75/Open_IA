from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import re
if __name__ == "__main__":
    client = GrobidClient(config_path="./config.json")
    client.process("processFulltextDocument", "./resources/test_pdf", output="./resources/out/", consolidate_citations=True, tei_coordinates=True, force=True)
    c = 0
    links = []
    figures = []
    folder = os.listdir('./resources/out')
    #print(folder)
    for file in folder:
    	ex = file.split('.')
    	if ex[len(ex)-1] == 'xml':
    		tree = ET.parse('./resources/out/'+file)
    		root = tree.getroot()
    		abstract_elements = root.findall('.//{http://www.tei-c.org/ns/1.0}abstract') #Accedemos al elemento abtract
    		#print(a[0].text)
    		for abstract in abstract_elements:
    			for div_element in abstract:
    				for p_element in div_element:
    					#print(p_element.text) #Accedemos al texto de abstract (P)
    					wordcloud = WordCloud(background_color = "white", max_words = 50).generate(p_element.text)
    					plt.imshow(wordcloud)
    					plt.axis("off")
    					plt.savefig("keyword_"+str(c))
    					c +=1
    		tree = ET.parse('./resources/out/'+file)
    		root = tree.getroot()
    		ref_elements = root.findall('.//{http://www.tei-c.org/ns/1.0}figure') #Accedemos al elemento figure
    		figures.append(len(ref_elements))
    		#print(div_elements)
    		#print("Numero figuras "+ str(len(ref_elements)))
    		tree = ET.parse('./resources/out/'+file)
    		root = tree.getroot()
    		p_elements = root.findall('.//{http://www.tei-c.org/ns/1.0}p') #Accedemos al elemento p
    		for p in p_elements:
    			link = p.text.split()
    			for linea in link:
    				if re.match('^http[s]*:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*',linea):
    					links.append(linea)
    		#print("Numero links " + str(len(links_elements)))
    #plt.hist(x=figures)
    #plt.show()
    print(figures)
    print(links)		
    		
    		
    		
    		
    		
