CountryLeaders = {'PL':'Duda','US':'Trump'}

##print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Merkel'

##print(CountryLeaders.keys())
##print(CountryLeaders.values())
##print(CountryLeaders.items())

##print(CountryLeaders.popitem())

##print(CountryLeaders.setdefault('FR','Macron'))

print(CountryLeaders.get('RU'))
NewLeaders = {'RU':'Putin','DE':'Schulz'}

CountryLeaders.update(NewLeaders)

print(CountryLeaders)
