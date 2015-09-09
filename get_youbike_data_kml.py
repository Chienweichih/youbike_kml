import urllib2  

website = 'http://its.taipei.gov.tw/atis_index/aspx/Youbike.aspx?Mode=1'
content = urllib2.urlopen(website).read()
lines = content.split('|')

output = '<?xml version="1.0" encoding="UTF-8"?>\n'
output += '<kml xmlns="http://earth.google.com/kml/2.2">\n'
output += '<Document>\n'
output += '\t<name>youbike</name>\n'

for oneLine in lines:
    tokens = oneLine.split('_')

    if len(tokens) != 12:
        break
    
    print tokens[1]
    output += '\t<Placemark>\n\t\t<name>'
    output += tokens[1]
    output += '</name>\n\t\t<description><![CDATA['
    output += tokens[7]
    output += ']]></description>\n\t\t<Point>\n\t\t\t<coordinates>'
    output += (tokens[6] + ',' + tokens[5]) 
    output += '</coordinates>\n\t\t</Point>\n\t</Placemark>\n'

output += '</Document>\n</kml>'

with open('youbike.kml', 'w') as f:
    f.write(output)
