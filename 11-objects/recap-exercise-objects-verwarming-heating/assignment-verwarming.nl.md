# Verwarming = Heating

Een architect moet verschillende verwarmingstoestellen plaatsen in een groot gebouw. Om een computersimulatie te kunnen maken van de warmteregeling van het gebouw, moet hij een reeks verwarmingstoestellen kunnen voorstellen. Hierbij wordt elk individueel verwarmingstoestel beschreven aan de hand van volgende informatievelden: 
* de naam van het toestel,
* de huidige instelling van de temperatuur,
* de minimum toegelaten temperatuur en
* de maximum toegelaten temperatuur.
* Binnen de simulatie moet de gewenste temperatuur van een bepaald toestel verhoogd of verlaagd kunnen worden, en moet de  ingestelde temperatuur van elke toestel te allen tijden kunnen opgevraagd worden.


### `TASK`
Definieer een klasse `Heating` die de volgende methoden bevat:

* Een constructor `__init__`, die vier parameters neemt:
  * `name`: de naam van het apparaat (een string)
  * `current_temp`: de temperatuurinstelling, gewenste temperatuur (int of float)
  * `min_temp`: de minimaal toegestane temperatuur (int of float)
  * `max_temp`: de maximaal toegestane temperatuur (int of float)
  * `name`, `min_temp`, en `max_temp` kunnen worden opgeslagen als openbare velden
  * `current_temp` moet privaat zijn en toegankelijk via een getter en een setter
    * De `current_temp` moet tussen `min_temp` en `max_temp` liggen.
    * Als de gewenste temperatuur lager zou zijn dan de minimumtemperatuur, dan moet de huidige temperatuur worden ingesteld op de minimumtemperatuur. Evenzo, als de gewenste temperatuur hoger zou zijn dan de maximumtemperatuur, dan moet de huidige temperatuur worden ingesteld op de maximumtemperatuur.
* Een methode `__repr__` die een tekenreeksrepresentatie van het verwarmingsapparaat (str) retourneert. Bekijk het onderstaande voorbeeld om te bepalen hoe deze tekenreeksweergave eruit moet zien. Alle getallen moeten worden weergegeven met één decimaal cijfer (gebruik afronding).
* Een methode `change_temperature` waarmee de huidige temperatuurinstelling kan worden gewijzigd. Een parameter, `temp_change` geeft aan hoeveel de huidige temperatuurinstelling moet worden gewijzigd. Als `temp_change` een positief getal is (int of float), wordt de huidige temperatuur verhoogd met de opgegeven hoeveelheid. Als `temp_change` negatief is, wordt de huidige temperatuur verlaagd. Natuurlijk moet de gewenste temperatuur binnen het toegestane bereik blijven.


#### USAGE
```python
>>> device1 = Heating('radiator kitchen', 20, 0, 100)
>>> device2 = Heating('radiator living room', 18, 15, 100)
>>> device3 = Heating('radiator bathroom', 22, 18, 28)
>>> print(device1)
Heating('radiator kitchen', 20.0, 0,.0 100.0)
>>> print(device2)
Heating('radiator living room', 18.0, 15.0, 100.0)
>>> device2.change_temperature(8)
>>> print(device2.get_desired_temp())
26.0
>>> device3.change_temperature(-5)
>>> print(device3)
Heating('radiator bathroom', 18.0, 18.0, 28.0)
```
