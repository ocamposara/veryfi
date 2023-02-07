# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:18:23 2023

@author: Sara Ocampo
"""
import json
import re

ruta = 'C:/Users/Sara Ocampo/Documents/Procesos de Selección/Veryfi/resources/'

with open(ruta + 'OCR_ticket2.json') as json_data:
    data = json.load(json_data)

pages = data.get('pages')[0].get('fullTextAnnotation').get('text')
listas = pages.split("\n")

##DATE
regex_date = "^\d{1,2}/\d{1,2}/\d{4}"
p = re.compile(regex_date)
for i in range(0,len(listas)):
    for m in p.finditer(listas[i]):
        date = m.group()

##ADDRESS
regex_add = "^(CALLE|AVENIDA|CARRERA|DIAGONAL){1}[a-zA-Z0-9\s]+-*\s*\d*"
p = re.compile(regex_add)
for i in range(0,len(listas)):
    for m in p.finditer(listas[i]):
        address = m.group()


####LINE ITEMS
##SKU
regex_sku = "^[0-9]{8,13}\s+"
sku = []

p = re.compile(regex_sku)
for i in range(0,len(listas)):
    for m in p.finditer(listas[i]):
        sku.append(m.group())
        
##DESCRIPTION
regex_description = "^[0-9]{8,13}\s+(\w+\s*\D+)"
description = []
p = re.compile(regex_description)
for i in range(0,len(listas)):
    for m in p.finditer(listas[i]):
        description.append(m.group(1))
        #print(m.groups(1))

##TOTAL - TAX CODE
regex_total_items = "(^\d{0,6}\s+)([A|N])"
total_items = []
tax_codes = []
p = re.compile(regex_total_items)
for i in range(0,len(listas)):
    for m in p.finditer(listas[i]):
        total_items.append(m.group(1))
        tax_codes.append(m.group(2))
        
##OUT
dict_out = {
   "date":date,
   "store_address":address,
   "line_items":{
      "sku":sku,
      "description":description,
      "total":total_items,
      "tax_codes":tax_codes
   }
}