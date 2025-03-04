teams = [
    "Ducks", "Bruins", "Sabres", 
    "Flames", "Hurricanes", "Blackhawks", "Avalanche", 
    "Blue_Jackets", "Stars", "Red_Wings", "Oilers", 
    "Panthers", "Kings", "Wild", "Canadiens", 
    "Predators", "Devils", "Islanders", "Rangers", 
    "Senators", "Flyers", "Penguins", "Sharks", 
    "Kraken", "Blues", "Lightning", "Maple_Leafs", "Hockey_Club", 
    "Canucks", "Golden_Knights", "Capitals", "Jets"]
positionsAI = ["C", "RW", "LW", "Def1", "Def2", "G"]
positionsUser = ["C", "RW", "LW", "Def1", "Def2", "G"]
used_players = []
used_Positions1 = []
used_Positions2 = []
# Anaheim Ducks
DucksC =  ["Trevor Zegras", "Ryan Strome", "Mason McTavish", "Leo Carlsson", "Isac Lundestrom", "Jansen Harkins"]
DucksLW = ["Alex Killorn", "Brock McGinn", "Cutter Gauthier", "Ross Johnston", "Frank Vatrano"]
DucksRW = ["Troy Terry", "Brett Leason", "Frank Vatrano"]
DucksDef1 = ["Jackson LaCombe", "Brian Dumoulin", "Radko Gudas", "Pavel Mintyukov", "Drew Helleson", "Olen Zellweger", "Jacob Trouba"]
DucksDef2 = ["Jackson LaCombe", "Brian Dumoulin", "Radko Gudas", "Pavel Mintyukov", "Drew Helleson", "Olen Zellweger", "Jacob Trouba"]
DucksG = ["John Gibson", "Lukas Dostal"]
#Bruins
BruinsC = ["John Beecher", "Charlie Coyle", "Trent Frederic", "Morgan Geekie", "Pavel Zacha", "Elias Lindholm", "Georgi Merkulov", "Matthew Poitras"]
BruinsLW = ["Brad Marchand", "Trent Frederic", "Taylor Hall", "Oliver Wahlstrom"]
BruinsRW = ["David Pastrnak", "Justin Brazeau", "Craig Smith", "Jakub Lauko"]
BruinsDef1 = ["Brandon Carlo", "Hampus Lindholm", "Charlie McAvoy", "Matt Grzelcyk", "Dmitry Orlov", "Mike Reilly", "Connor Clifton", "Mason Lohrei", "Michael Callahan", "Nikita Zadorov"]
BruinsDef2 = ["Brandon Carlo", "Hampus Lindholm", "Charlie McAvoy", "Matt Grzelcyk", "Dmitry Orlov", "Mike Reilly", "Connor Clifton", "Mason Lohrei", "Michael Callahan", "Nikita Zadorov"]
BruinsG = ["Jeremy Swayman", "Joonas Korpisalo"]

#Sabres
SabresC = ["Dylan Cozens", "Peyton Krebs", "Jiri Kulich", "Sam Lafferty", "Ryan McLeod", "Tage Thompson"]
SabresLW = ["Zach Benson", "Jordan Greenway", "Beck Malenstyn"]
SabresRW = ["Alex Tuch", "JJ Peterka", "Jack Quinn"]
SabresDef1 = ["Jacob Bryson", "Bowen Byram", "Connor Clifton", "Rasmus Dahlin", "Mattias Samuelsson"]
SabresDef2 = ["Jacob Bryson", "Bowen Byram", "Connor Clifton", "Rasmus Dahlin", "Mattias Samuelsson"]
SabresG = ["Ukko-Pekka Luukkonen", "James Reimer"]

#Flames
FlamesC = ["Mikael Backlund", "Morgan Frost", "Nazem Kadri", "Jared McCann", "Martin Pospisil", "Kevin Rooney", "Yegor Sharangovich", "Connor Zary"]
FlamesLW = ["Jonathan Huberdeau", "Blake Coleman", "Anthony Mantha", "Sam Honzek"]
FlamesRW = ["Matt Coronato", "Jack Quinn", "Joel Farabee"]
FlamesDef1 = ["Rasmus Andersson", "Kevin Bahl", "Tyson Barrie", "Jake Bean", "Joel Hanley", "MacKenzie Weegar", "Daniil Miromanov", "Brayden Pachal"]
FlamesDef2 = ["Rasmus Andersson", "Kevin Bahl", "Tyson Barrie", "Jake Bean", "Joel Hanley", "MacKenzie Weegar", "Daniil Miromanov", "Brayden Pachal"]
FlamesG = ["Dustin Wolf", "Dan Vladar"]

#Hurricanes
HurricanesC = ["Sebastian Aho", "Jesperi Kotkaniemi", "Jack Roslovic", "Jordan Staal", "Jesperi Kotkaniemi"]
HurricanesLW = ["Taylor Hall", "Seth Jarvis", "Jordan Martinook", "William Carrier"]
HurricanesRW = ["Mikko Rantanen", "Jackson Blake"]
HurricanesDef1 = ["Brent Burns", "Jalen Chatfield", "Shayne Gostisbehere", "Dmitri Orlov", "Jaccob Slavin"]
HurricanesDef2 = ["Brent Burns", "Jalen Chatfield", "Shayne Gostisbehere", "Dmitri Orlov", "Jaccob Slavin"]
HurricanesG = ["Frederik Andersen"]

#Blackhawks
BlackhawksC= ["Connor Bedard", "Teuvo Teravainen", "Philipp Kurashev", "Jason Dickinson", "Ryan Donato", "Andreas Athanasiou", "Frank Nazar", "Colton Dach", "Petr Mrazek"]
BlackhawksLW = ["Tyler Bertuzzi", "Taylor Hall", "Pat Maroon", "Lucas Reichel", "Andreas Athanasiou"]
BlackhawksRW = ["Ilya Mikheyev", "Patrick Kane", "Tyler Johnson", "Reese Johnson", "Andreas Athanasiou"]
BlackhawksDef1 = ["Connor Murphy", "Kevin Korchinski", "Alec Martinez", "Nolan Allan", "T.J. Brodie", "Louis Crevier", "Ethan Del Mastro", "Alex Vlasic"]
BlackhawksDef2 = ["Connor Murphy", "Kevin Korchinski", "Alec Martinez", "Nolan Allan", "T.J. Brodie", "Louis Crevier", "Ethan Del Mastro", "Alex Vlasic"]
BlackhawksG = ["Petr Mrazek", "Arvid Soderblom", "Spencer Knight"]

#Avalanche
AvalancheC = ["Nathan MacKinnon", "Casey Mittelstadt", "Jack Drury", "Ross Colton", "Parker Kelly"]
AvalancheLW = ["Artturi Lehkonen", "Jonathan Drouin", "Gabriel Landeskog"]
AvalancheRW = ["Martin Necas", "Ross Colton", "Logan O'Connor"]
AvalancheDef1 = ["Cale Makar", "Sam Girard", "Ryan Lindgren", "Josh Manson", "Bowen Byram", "Kurtis MacDermid", "Jacob MacDonald"]
AvalancheDef2 = ["Cale Makar", "Sam Girard", "Ryan Lindgren", "Josh Manson", "Bowen Byram", "Kurtis MacDermid", "Jacob MacDonald"]
AvalancheG = ["Mackenzie Blackwood", "Pavel Francouz"]

#Blue Jackets
Blue_JacketsC = ["Zach Aston-Reese", "Adam Fantilli", "Boone Jenner", "Kent Johnson", "Sean Kuraly", "Joseph LaBate", "Cole Sillinger"]
Blue_JacketsLW = ["James van Riemsdyk", "Dmitri Voronkov", "Mikael Pyyhtia", "Kirill Marchenko"]
Blue_JacketsRW = ["Yegor Chinakhov", "Justin Danforth", "Mathieu Olivier"]
Blue_JacketsDef1 = ["Jake Christiansen", "Jack Johnson", "Zach Werenski", "Ivan Provorov", "Jordan Harris", "Erik Gudbranson", "David Jiricek", "Damon Severson", "Dante Fabbro"]
Blue_JacketsDef2 = ["Jake Christiansen", "Jack Johnson", "Zach Werenski", "Ivan Provorov", "Jordan Harris", "Erik Gudbranson", "David Jiricek", "Damon Severson", "Dante Fabbro"]
Blue_JacketsG = ["Elvis Merzlikins", "Jonas Korpisalo"]

#Stars
StarsC = ["Wyatt Johnston", "Roope Hintz", "Matt Duchene", "Mikael Granlund", "Colin Blackwell", "Oskar Bäck", "Mavrik Bourque"]
StarsLW = ["Jason Robertson", "Jamie Benn", "Evgenii Dadonov", "Logan Stankoven"]
StarsRW = ["Tyler Seguin", "Marian Studenic"]
StarsDef1 = ["Miro Heiskanen", "Esa Lindell", "Thomas Harley", "Cody Ceci", "Matt Dumba", "Lian Bichsel"]
StarsDef2 = ["Miro Heiskanen", "Esa Lindell", "Thomas Harley", "Cody Ceci", "Matt Dumba", "Lian Bichsel"]
StarsG = ["Jake Oettinger", "Scott Wedgewood"]

#Red Wings
Red_WingsC = ["Dylan Larkin", "Andrew Copp", "Michael Rasmussen", "Joe Veleno", "Marco Kasper", "Tyler Motte"]
Red_WingsLW = ["Lucas Raymond", "J.T. Compher", "David Perron"]
Red_WingsRW = ["Lucas Raymond","Alex DeBrincat","Vladimir Tarasenko","Jonatan Berggren"]
Red_WingsDef1 = ["Ben Chiarot", "Simon Edvinsson", "Moritz Seider", "Jared McIsaac", "Gustav Lindström", "Jake Walman"]
Red_WingsDef2 = ["Ben Chiarot", "Simon Edvinsson", "Moritz Seider", "Jared McIsaac", "Gustav Lindström", "Jake Walman"]
Red_WingsG = ["Ville Husso", "Alex Lyon", "Cam Talbot"]

#Oilers
OilersC = ["Connor McDavid", "Leon Draisaitl", "Ryan Nugent-Hopkins", "Ryan Savoie", "Adam Henrique", "Mattias Janmark"]
OilersLW = ["Zach Hyman", "Viktor Arvidsson", "Jeff Skinner"]
OilersRW = ["Kailer Yamamoto", "Connor Brown", "Tyler Benson"]
OilersDef1 = ["Evan Bouchard", "Mattias Ekholm", "Darnell Nurse", "Cody Ceci", "Brett Kulak", "Ty Emberson", "John Klingberg"]
OilersDef2 = ["Evan Bouchard", "Mattias Ekholm", "Darnell Nurse", "Cody Ceci", "Brett Kulak", "Ty Emberson", "John Klingberg"]
OilersG = ["Stuart Skinner", "Jack Campbell"]

#Panthers
PanthersC = ["Aleksander Barkov", "Sam Bennett", "Jesper Boqvist", "Anton Lundell", "Eetu Luostarinen", "Sam Reinhart", "Evan Rodrigues", "Carter Verhaeghe"]
PanthersLW = ["Matthew Tkachuk", "Ryan Lomberg"]
PanthersRW = ["Sam Reinhart", "Evan Rodrigues"]
PanthersDef1 = ["Aaron Ekblad", "Gustav Forsling", "Seth Jones", "Dmitri Kulikov", "Uvis Balinskis", "Tobias Bjornfot"]
PanthersDef2 = ["Aaron Ekblad", "Gustav Forsling", "Seth Jones", "Dmitri Kulikov", "Uvis Balinskis", "Tobias Bjornfot"]
PanthersG = ["Sergei Bobrovsky"]

#Kings
KingsC = ["Anze Kopitar", "Phillip Danault", "Quinton Byfield", "Jack Studnicka"]
KingsLW = ["Kevin Fiala", "Alex Turcotte", "Warren Foegele", "Tanner Jeannot"]
KingsRW = ["Adrian Kempe", "Trevor Moore", "Alex Laferriere", "Trevor Lewis"]
KingsDef1 = ["Mikey Anderson", "Joel Edmundson", "Jacob Moverare", "Drew Doughty", "Vladislav Gavrikov", "Jordan Spence", "Caleb Jones"]
KingsDef2 = ["Mikey Anderson", "Joel Edmundson", "Jacob Moverare", "Drew Doughty", "Vladislav Gavrikov", "Jordan Spence", "Caleb Jones"]
KingsG = ["Darcy Kuemper", "David Rittich"]

#Wild
WildC = ["Joel Eriksson Ek", "Frederick Gaudreau", "Brendan Gaunce", "Vinnie Hinostroza", "Marcus Johansson", "Jakub Lauko", "Gustav Nyquist", "Marco Rossi", "Devin Shore", "Yakov Trenin"]
WildLW = ["Matt Boldy", "Kirill Kaprizov"]
WildRW = ["Ryan Hartman", "Mats Zuccarello"]
WildDef1 = ["Jonas Brodin", "Declan Chisholm", "Brock Faber", "Jon Merrill", "Jacob Middleton", "Jared Spurgeon", "Zach Bogosian"]
WildDef2 = ["Jonas Brodin", "Declan Chisholm", "Brock Faber", "Jon Merrill", "Jacob Middleton", "Jared Spurgeon", "Zach Bogosian"]
WildG = ["Marc-Andre Fleury", "Filip Gustavsson", "Jesper Wallstedt"]

#Canadiens
CanadiensC = ["Nick Suzuki", "Kirby Dach", "Alex Newhook", "Christian Dvorak", "Jake Evans", "Owen Beck"]
CanadiensLW = ["Josh Anderson", "Cole Caufield", "Mike Hoffman", "Rafael Harvey-Pinard", "Juraj Slafkovsky"]
CanadiensRW = ["Joel Armia", "Brendan Gallagher", "Jonathan Drouin", "Evgenii Dadonov"]
CanadiensDef1 = ["Kaiden Guhle", "Jordan Harris", "David Savard", "Arber Xhekaj", "Lane Hutson", "Alexandre Carrier" "Mike Matheson", "Justin Barron", "Johnathan Kovacevic"]
CanadiensDef2 = ["Kaiden Guhle", "Jordan Harris", "David Savard", "Arber Xhekaj", "Lane Hutson", "Alexandre Carrier" "Mike Matheson", "Justin Barron", "Johnathan Kovacevic"]
CanadiensG = ["Samuel Montembeault", "Jake Allen", "Jakub Dobes"]

#Predators
PredatorsC = ["Steven Stamkos", "Tommy Novak", "Mark Jankowski", "Jacob Lucchini", "Jonathan Marchessault"]
PredatorsLW = ["Filip Forsberg", "Zachary L'Heureux", "Colton Sissons"]
PredatorsRW = ["Luke Evangelista", "Michael McCarron"]
PredatorsDef1 = ["Roman Josi", "Brady Skjei", "Jérémy Lauzon", "Andreas Englund", "Adam Wilsby", "Nick Blankenburg", "Luke Schenn"]
PredatorsDef2 = ["Roman Josi", "Brady Skjei", "Jérémy Lauzon", "Andreas Englund", "Adam Wilsby", "Nick Blankenburg", "Luke Schenn"]
PredatorsG = ["Juuse Saros", "Kevin Lankinen"]

#Devils
DevilsC = ["Nico Hischier", "Jack Hughes", "Dawson Mercer", "Paul Cotter", "Johan Larsson", "Erik Haula"]
DevilsLW = ["Jesper Bratt", "Ondrej Palat", "Tomas Tatar", "Alexander Holtz", "Adam Beckman"]
DevilsRW = ["Timo Meier", "Stefan Noesen", "Nathan Bastian", "Jesper Boqvist", "Mikhail Maltsev"]
DevilsDef1 = ["Dougie Hamilton", "Jonas Siegenthaler", "Brenden Dillon", "Brett Pesce", "Luke Hughes", "Johnathan Kovacevic", "Seamus Casey"]
DevilsDef2 = ["Dougie Hamilton", "Jonas Siegenthaler", "Brenden Dillon", "Brett Pesce", "Luke Hughes", "Johnathan Kovacevic", "Seamus Casey"]
DevilsG = ["Jacob Markstrom", "Nico Daws"]

#Islanders
IslandersC = ["Mathew Barzal", "Casey Cizikas", "Marc Gatcomb", "Bo Horvat", "Kyle MacLean", "Brock Nelson", "Jean-Gabriel Pageau"]
IslandersLW = ["Anthony Duclair", "Pierre Engvall", "Anders Lee"]
IslandersRW = ["Hudson Fasching", "Kyle Palmieri"]
IslandersDef1 = ["Adam Pelech", "Alexander Romanov", "Ryan Pulock", "Noah Dobson", "Scott Perunovich"]
IslandersDef2 = ["Adam Pelech", "Alexander Romanov", "Ryan Pulock", "Noah Dobson", "Scott Perunovich"]
IslandersG = ["Ilya Sorokin", "Semyon Varlamov"]

#Rangers
RangersC = ["Filip Chytil", "Sam Carrick", "Jonny Brodzinski", "Juuso Parssinen"]
RangersLW = ["Chris Kreider", "Will Cuylle", "Brett Berard", "Reilly Smith", "Alexis Lafreniere", "Artemi Panarin"]
RangersRW = ["Mika Zibanejad", "Kaapo Kakko", "Vincent Trocheck", "Julien Gauthier"]
RangersDef1 = ["Ryan Lindgren", "K'Andre Miller", "Zac Jones", "Adam Fox", "Calvin de Haan", "Will Borgen", "Braden Schneider"]
RangersDef2 = ["Ryan Lindgren", "K'Andre Miller", "Zac Jones", "Adam Fox", "Calvin de Haan", "Will Borgen", "Braden Schneider"]
RangersG = ["Igor Shesterkin", "Jonathan Quick"]

#Senators
SenatorsC = ["Tim Stützle", "Josh Norris", "Shane Pinto", "Ridly Greig", "Nick Cousins", "Michael Amadio"]
SenatorsLW = ["Brady Tkachuk", "Mathieu Joseph", "Parker Kelly", "David Perron"]
SenatorsRW = ["Drake Batherson", "Claude Giroux", "Adam Gaudette"]
SenatorsDef1 = ["Thomas Chabot", "Jake Sanderson", "Tyler Kleven", "Nick Jensen", "Travis Hamonic", "Jacob Bernard-Docker"]
SenatorsDef2 = ["Thomas Chabot", "Jake Sanderson", "Tyler Kleven", "Nick Jensen", "Travis Hamonic", "Jacob Bernard-Docker"]
SenatorsG = ["Linus Ullmark", "Anton Forsberg"]

# Flyers
FlyersC = ["Sean Couturier", "Scott Laughton", "Ryan Poehling", "Noah Cates"]
FlyersLW = ["Tyson Foerster", "Nicolas Deslauriers"]
FlyersRW = ["Travis Konecny", "Bobby Brink", "Andrei Kuzmenko", "Jakob Pelletier", "Matvei Michkov"]
FlyersDef1 = ["Jamie Drysdale", "Erik Johnson", "Rasmus Ristolainen", "Travis Sanheim", "Nick Seeler", "Cam York", "Egor Zamula"]
FlyersDef2 = ["Jamie Drysdale", "Erik Johnson", "Rasmus Ristolainen", "Travis Sanheim", "Nick Seeler", "Cam York", "Egor Zamula"]
FlyersG = ["Samuel Ersson", "Ivan Fedotov"]

#Penguins
PenguinsC = ["Sidney Crosby", "Evgeni Malkin", "Cody Glass", "Lars Eller", "Noel Acciari"]
PenguinsLW = ["Michael Bunting", "Anthony Beauvillier", "Drew O'Connor", "Valtteri Puustinen"]
PenguinsRW = ["Rickard Rakell", "Bryan Rust", "Kevin Hayes", "Jesse Puljujarvi"]
PenguinsDef1 = ["Ryan Graves", "Matt Grzelcyk", "Pierre-Olivier Joseph", "Ryan Shea", "Kris Letang", "Erik Karlsson", "Jack St. Ivany"]
PenguinsDef2 = ["Ryan Graves", "Matt Grzelcyk", "Pierre-Olivier Joseph", "Ryan Shea", "Kris Letang", "Erik Karlsson", "Jack St. Ivany"]
PenguinsG = ["Tristan Jarry", "Alex Nedeljikovic"]

#Sharks
SharksC = ["Macklin Celebrini", "Logan Couture", "Ty Dellandrea", "Thomas Bordeleau", "Nico Sturm"]
SharksLW = ["William Eklund", "Alexander Barabanov", "Filip Zadina", "Oskar Lindblom"]
SharksRW = ["Kevin Labanc", "Luke Kunin", "Egor Afanasyev", "Walker Duehr"]
SharksDef1 = ["Mario Ferraro", "Marc-Edouard Vlasic", "Nikita Okhotiuk", "Jan Rutta", "Matt Benning", "Henry Thrun"]
SharksDef2 = ["Mario Ferraro", "Marc-Edouard Vlasic", "Nikita Okhotiuk", "Jan Rutta", "Matt Benning", "Henry Thrun"]
SharksG = ["Alexandar Georgiev", "Kappo Kahkonen"]

#Kraken
KrakenC = ["Matty Beniers", "Chandler Stephenson", "Jaden Schwartz", "Ben Meyers", "Yanni Gourde", "Mitchell Stephens", "Tye Kartye"]
KrakenLW = ["Jared McCann", "Brandon Tanev", "Eeli Tolvanen"]
KrakenRW = ["Jordan Eberle", "Oliver Bjorkstrand", "Kaapo Kakko", "John Hayden"]
KrakenDef1 = ["Vince Dunn", "Jamie Oleksiak", "Carson Soucy", "Adam Larsson", "Justin Schultz", "Cale Fleury"]
KrakenDef2 = ["Vince Dunn", "Jamie Oleksiak", "Carson Soucy", "Adam Larsson", "Justin Schultz", "Cale Fleury"]
KrakenG = ["Philipp Grubauer", "Chris Driedger"]

#Blues
BluesC = ["Brayden Schenn", "Robert Thomas", "Radek Faksa", "Oskar Sundqvist", "Zachary Bolduc"]
BluesLW = ["Pavel Buchnevich", "Nathan Walker"]
BluesRW = ["Jordan Kyrou", "Kasperi Kapanen", "Alexei Toropchenko", "Mathieu Joseph"]
BluesDef1 = ["Nick Leddy", "Torey Krug", "Marco Scandella", "Scott Perunovich", "Tyler Tucker", "Colton Parayko", "Justin Faulk", "Cam Fowler", "Robert Bortuzzo"]
BluesDef2 = ["Nick Leddy", "Torey Krug", "Marco Scandella", "Scott Perunovich", "Tyler Tucker", "Colton Parayko", "Justin Faulk", "Cam Fowler", "Robert Bortuzzo"]
BluesG = ["Jordan Binnington", "Joel Hofer"]

#Lightning
LightningC = ["Anthony Cirelli", "Zemgus Girgensons", "Luke Glendening", "Brayden Point", "Jake Guentzel"]
LightningLW = ["Mikey Eyssimont", "Brandon Hagel"]
LightningRW = ["Cam Atkinson", "Mitchell Chaffee", "Nikita Kucherov"]
LightningDef1 = ["Victor Hedman", "Erik Cernak", "Darren Raddysh"]
LightningDef2 = ["Victor Hedman", "Erik Cernak", "Darren Raddysh"]
LightningG = ["Andrei Vasilevskiy", "Hugo Alnefelt"]

#Maple_Leafs
Maple_LeafsC = ["Auston Matthews", "John Tavares", "Max Domi", "David Kampf", "Calle Jarnkrok", "Connor Dewar", "Steven Lorentz", "Bobby McMann", "Alex Steeves"]
Maple_LeafsLW = ["Nicholas Robertson", "Matthew Knies", "Max Domi"]
Maple_LeafsRW = ["William Nylander", "Mitch Marner", "Sam Lafferty", "Ryan Reaves"]
Maple_LeafsDef1 = ["Morgan Rielly", "Jake McCabe", "Simon Benoît", "Oliver Ekman-Larsson", "Chris Tanev", "Jani Hakanpaa", "Timothy Liljegren"]
Maple_LeafsDef2 = ["Morgan Rielly", "Jake McCabe", "Simon Benoît", "Oliver Ekman-Larsson", "Chris Tanev", "Jani Hakanpaa", "Timothy Liljegren"]
Maple_LeafsG = ["Anthony Stolarz", "Joseph Woll"]

#Hockey_Club
Hockey_ClubC = ["Logan Cooley", "Jack McBain", "Barrett Hayton" "Alexander Kerfoot", "Kevin Stenlund"]
Hockey_ClubLW = ["Clayton Keller", "Lawson Crouse", "Matias Maccelli", "Michael Carcone", "Liam O'Brien"]
Hockey_ClubRW = ["Dylan Guenther", "Nick Bjugstad", "Nick Schmaltz", "Josh Doan"]
Hockey_ClubDef1 = ["Mikhail Sergachev", "Ian Cole", "Michael Kesselring", "Sean Durzi", "Olli Maata", "John Marino", "Shea Weber", "Nick DeSimone"]
Hockey_ClubDef2 = ["Mikhail Sergachev", "Ian Cole", "Michael Kesselring", "Sean Durzi", "Olli Maata", "John Marino", "Shea Weber", "Nick DeSimone"]
Hockey_ClubG = ["Karel Vejmelka", "Connor Ingram"]

#Canucks
CanucksC = ["Elias Pettersson", "Filip Chytil", "Pius Suter", "Nils Aman", "Teddy Blueger", "Drew O'Connor"]
CanucksLW = ["Ilya Mikheyev", "Conor Garland", "Kiefer Sherwood"]
CanucksRW = ["Brock Boeser", "Anthony Beauvillier", "Dakota Joshua"]
CanucksDef1 = ["Quinn Hughes", "Filip Hronek", "Marcus Pettersson", "Victor Mancini", "Tyler Myers", "Filip Hronek"]
CanucksDef2 = ["Quinn Hughes", "Filip Hronek", "Marcus Pettersson", "Victor Mancini", "Tyler Myers", "Filip Hronek"]
CanucksG = ["Thatcher Demko", "Arturs Silovs"]

#Golden_Knights
Golden_KnightsC = ["Ivan Barbashev", "Jack Eichel", "Tomas Hertl", "Brett Howden", "William Karlsson", "Rafael Lavoie", "Nicolas Roy"]
Golden_KnightsLW = ["Pavel Dorofeyev", "Brandon Saad", "Cole Schwindt", "Kaedan Korczak"]
Golden_KnightsRW = ["Phil Kessel", "Keegan Kolesar", "Michael Amadio", "Paul Cotter"]
Golden_KnightsDef1 = ["Shea Theodore", "Alec Martinez", "Nicolas Hague", "Brayden McNabb", "Ben Hutton", "Alex Pietrangelo", "Zach Whitecloud", "Kaedan Korczak"]
Golden_KnightsDef2 = ["Shea Theodore", "Alec Martinez", "Nicolas Hague", "Brayden McNabb", "Ben Hutton", "Alex Pietrangelo", "Zach Whitecloud", "Kaedan Korczak"]
Golden_KnightsG = ["Adin Hill", "Ilya Samsonov"]

#Capitals
CapitalsC = [ "Nic Dowd", "Lars Eller", "Aliaksei Protas", "Connor McMichael", "Dylan Strome", "Pierre-Luc Dubois"]
CapitalsLW = ["Alex Ovechkin", "Tom Wilson", "Andrew Mangiapane", "Brandon Duhaime"]
CapitalsRW = ["Taylor Raddysh", "Ethen Frank", "Matt Roy"]
CapitalsDef1 = ["Jakob Chychrun", "Rasmus Sandin", "Martin Fehervary", "Matt Roy", "John Carlson", "Trevor van Riemsdyk", "Nick Jensen", "Brenden Dillon"]
CapitalsDef2 = ["Jakob Chychrun", "Rasmus Sandin", "Martin Fehervary", "Matt Roy", "John Carlson", "Trevor van Riemsdyk", "Nick Jensen", "Brenden Dillon"]
CapitalsG = ["Charlie Lindgren", "Logan Thompson"]

#Jets
JetsC = ["Morgan Barron", "David Gustafsson", "Rasmus Kupari", "Adam Lowry", "Vladislav Namestnikov", "Cole Perfetti", "Mark Scheifele", "Gabriel Vilardi"]
JetsLW = ["Kyle Connor", "Nikolaj Ehlers", "Alex Iafallo", "Nino Niederreiter"]
JetsRW = ["Cole Perfetti", "Mason Appleton", "Gabriel Vilardi"]
JetsDef1 = ["Dylan DeMelo", "Dylan Samberg", "Haydn Fleury", "Ville Heinola", "Josh Morrissey", "Neal Pionk", "Colin Miller", "Logan Stanley"]
JetsDef2 = ["Dylan DeMelo", "Dylan Samberg", "Haydn Fleury", "Ville Heinola", "Josh Morrissey", "Neal Pionk", "Colin Miller", "Logan Stanley"]
JetsG = ["Connor Hellebuyck", "Eric Comrie"]
