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
positionsUser1 = ["C", "RW", "LW", "Def1", "Def2", "G"]
positionsUser2 = ["C", "RW", "LW", "Def1", "Def2", "G"]
used_players = []
used_Positions1 = []
used_Positions2 = []
# Anaheim Ducks
DucksC =  ["Trevor Zegras", "Ryan Strome", "Mason McTavish", "Leo Carlsson", "Isac Lundestrom", "Jansen Harkins", "Robby Fabbri"]
DucksLW = ["Alex Killorn", "Brock McGinn", "Cutter Gauthier", "Ross Johnston"]
DucksRW = ["Troy Terry", "Brett Leason", "Frank Vatrano", "Sam Colangelo"]
DucksDef1 = ["Jackson LaCombe", "Radko Gudas", "Pavel Mintyukov", "Drew Helleson", "Olen Zellweger", "Jacob Trouba", "Oliver Kylington"]
DucksDef2 = ["Jackson LaCombe", "Radko Gudas", "Pavel Mintyukov", "Drew Helleson", "Olen Zellweger", "Jacob Trouba", "Oliver Kylington"]
DucksG = ["John Gibson", "Lukas Dostal", "Ville Husso"]
#Bruins
BruinsC = ["John Beecher", "Jakub Lauko", "Morgan Geekie", "Pavel Zacha", "Elias Lindholm", "Patrick Brown", "Mark Kastelic", "Marat Khusnutdinov", "Vinni Lettieri", "Casey Mittelstadt"]
BruinsLW = ["Cole Koepke"]
BruinsRW = ["David Pastrnak"]
BruinsDef1 = ["Henri Jokiharju", "Hampus Lindholm", "Charlie McAvoy", "Mason Lohrei", "Ian Mitchell", "Andrew Peeke", "Parker Wotherspoon", "Nikita Zadorov"]
BruinsDef2 = ["Henri Jokiharju", "Hampus Lindholm", "Charlie McAvoy", "Mason Lohrei", "Ian Mitchell", "Andrew Peeke", "Parker Wotherspoon", "Nikita Zadorov"]
BruinsG = ["Jeremy Swayman", "Joonas Korpisalo"]

#Sabres
SabresC = ["Josh Dunne", "Peyton Krebs", "Jiri Kulich", "Sam Lafferty", "Ryan McLeod", "Josh Norris" "Tage Thompson"]
SabresLW = ["Zach Benson", "Jordan Greenway", "Beck Malenstyn", "Jason Zucker"]
SabresRW = ["Alex Tuch", "JJ Peterka", "Jack Quinn", "Isak Rosen"]
SabresDef1 = ["Jacob Bernard-Docker", "Jacob Bryson", "Bowen Byram", "Connor Clifton", "Rasmus Dahlin", "Mattias Samuelsson", "Owen Power"]
SabresDef2 = ["Jacob Bernard-Docker", "Jacob Bryson", "Bowen Byram", "Connor Clifton", "Rasmus Dahlin", "Mattias Samuelsson", "Owen Power"]
SabresG = ["Ukko-Pekka Luukkonen", "James Reimer"]

#Flames
FlamesC = ["Mikael Backlund", "Morgan Frost", "Nazem Kadri", "Justin Kirkland", "Martin Pospisil", "Kevin Rooney", "Yegor Sharangovich", "Connor Zary"]
FlamesLW = ["Jonathan Huberdeau","Joel Farabee", "Blake Coleman", "Ryan Lomberg"]
FlamesRW = ["Matt Coronato", "Anthony Mantha"]
FlamesDef1 = ["Rasmus Andersson", "Kevin Bahl", "Ilya Solovyov", "Jake Bean", "Joel Hanley", "MacKenzie Weegar", "Daniil Miromanov", "Brayden Pachal"]
FlamesDef2 = ["Rasmus Andersson", "Kevin Bahl", "Ilya Solovyov", "Jake Bean", "Joel Hanley", "MacKenzie Weegar", "Daniil Miromanov", "Brayden Pachal"]
FlamesG = ["Dustin Wolf", "Dan Vladar"]

#Hurricanes
HurricanesC = ["Sebastian Aho", "Jesperi Kotkaniemi", "Jack Roslovic", "Jordan Staal", "Mark Jankowski", "Seth Jarvis", "Tyson Jost", "Logan Stankoven"]
HurricanesLW = ["Taylor Hall", "Jordan Martinook", "William Carrier", "Eric Robinson"]
HurricanesRW = ["Andrei Svechnikov", "Jackson Blake"]
HurricanesDef1 = ["Brent Burns", "Jalen Chatfield", "Shayne Gostisbehere", "Dmitry Orlov", "Jaccob Slavin", "Riley Stillman", "Sean Walker"]
HurricanesDef2 = ["Brent Burns", "Jalen Chatfield", "Shayne Gostisbehere", "Dmitry Orlov", "Jaccob Slavin", "Riley Stillman", "Sean Walker"]
HurricanesG = ["Frederik Andersen", "Pyotr Kochetkov"]

#Blackhawks
BlackhawksC= ["Connor Bedard", "Teuvo Teravainen", "Philipp Kurashev", "Jason Dickinson", "Ryan Donato", "Frank Nazar", "Colton Dach", "Joe Veleno"]
BlackhawksLW = ["Tyler Bertuzzi", "Nick Foligno", "Patrick Maroon", "Lucas Reichel", "Landon Slaggert", "Ilya Mikheyev"]
BlackhawksRW = ["Ilya Mikheyev", "Patrick Kane", "Tyler Johnson", "Reese Johnson", "Andreas Athanasiou"]
BlackhawksDef1 = ["Connor Murphy", "Artyom Levshunov", "Alec Martinez", "Wyatt Kaiser", "T.J. Brodie", "Louis Crevier", "Ethan Del Mastro", "Alex Vlasic"]
BlackhawksDef2 = ["Connor Murphy", "Artyom Levshunov", "Alec Martinez", "Wyatt Kaiser", "T.J. Brodie", "Louis Crevier", "Ethan Del Mastro", "Alex Vlasic"]
BlackhawksG = ["Arvid Soderblom", "Spencer Knight"]

#Avalanche
AvalancheC = ["Nathan MacKinnon", "Charlie Coyle", "Jack Drury", "Brock Nelson ", "Parker Kelly", "Martin Necas", "Ross Colton"]
AvalancheLW = ["Artturi Lehkonen", "Jonathan Drouin", "Joel Kiviranta", "Jimmy Vesey", "Miles Wood"]
AvalancheRW = ["Valeri Nichushkin", "Logan O'Connor"]
AvalancheDef1 = ["Cale Makar", "Samuel Girard", "Ryan Lindgren", "Josh Manson", "Erik Johnson", "Sam Malinski", "Keaton Middleton", "Devon Toews"]
AvalancheDef2 = ["Cale Makar", "Samuel Girard", "Ryan Lindgren", "Josh Manson", "Erik Johnson", "Sam Malinski", "Keaton Middleton", "Devon Toews"]
AvalancheG = ["Mackenzie Blackwood", "Scott Wedgewood"]

#Blue Jackets
Blue_JacketsC = ["Zachary Aston-Reese", "Adam Fantilli", "Boone Jenner", "Kent Johnson", "Sean Kuraly", "Sam Monahan", "Cole Sillinger", "Luke Kunin"]
Blue_JacketsLW = ["James van Riemsdyk", "Dmitri Voronkov"]
Blue_JacketsRW = ["Yegor Chinakhov", "Justin Danforth", "Mathieu Olivier", "Christian Fischer", "Kirill Marchenko", "Kevin Lebanc"]
Blue_JacketsDef1 = ["Jake Christiansen", "Jack Johnson", "Zach Werenski", "Ivan Provorov", "Jordan Harris", "Erik Gudbranson", "Damon Severson", "Dante Fabbro", "Denton Mateychuk"]
Blue_JacketsDef2 = ["Jake Christiansen", "Jack Johnson", "Zach Werenski", "Ivan Provorov", "Jordan Harris", "Erik Gudbranson", "Damon Severson", "Dante Fabbro", "Denton Mateychuk"]
Blue_JacketsG = ["Elvis Merzlikins", "Daniil Tarasov"]

#Stars
StarsC = ["Wyatt Johnston", "Roope Hintz", "Matt Duchene", "Mikael Granlund", "Colin Blackwell", "Oskar Bäck", "Mavrik Bourque", "Tyler Seguin", "Sam Steel"]
StarsLW = ["Jason Robertson", "Jamie Benn", "Jamie Benn"]
StarsRW = ["Evengii Dadonov", "Mikko Rantanen"]
StarsDef1 = ["Miro Heiskanen", "Esa Lindell", "Thomas Harley", "Cody Ceci", "Matt Dumba", "Lian Bichsel", "Nils Lundkvist", "Ilya Lyubushkin", "Brendan smith"]
StarsDef2 = ["Miro Heiskanen", "Esa Lindell", "Thomas Harley", "Cody Ceci", "Matt Dumba", "Lian Bichsel", "Nils Lundkvist", "Ilya Lyubushkin", "Brendan smith"]
StarsG = ["Jake Oettinger", "Casey DeSmith"]

#Red Wings
Red_WingsC = ["Dylan Larkin", "Andrew Copp", "Michael Rasmussen", "Craig Smith", "Marco Kasper", "Tyler Motte"]
Red_WingsLW = ["Lucas Raymond", "J.T. Compher", "Carter Mazur", "Elmer Soderblom"]
Red_WingsRW = ["Patrick Kane","Alex DeBrincat", "Vladimir Tarasenko","Jonatan Berggren", "Dominik Shine"]
Red_WingsDef1 = ["Ben Chiarot", "Simon Edvinsson", "Moritz Seider", "Justin Holl", "Albert Johansson", "Erik Gustafsson", "William Lagesson", "Jeff Petry"]
Red_WingsDef2 = ["Ben Chiarot", "Simon Edvinsson", "Moritz Seider", "Justin Holl", "Albert Johansson", "Erik Gustafsson", "William Lagesson", "Jeff Petry"]
Red_WingsG = ["Petr Mrazek", "Alex Lyon", "Cam Talbot"]

#Oilers
OilersC = ["Connor McDavid", "Leon Draisaitl", "Ryan Nugent-Hopkins", "Trent Frederic", "Adam Henrique", "Mattias Janmark", "Jeff SKinner"]
OilersLW = ["Zach Hyman", "Viktor Arvidsson", "Max Jones"]
OilersRW = ["Kasperi Kapanen", "Connor Brown", "Corey Perry", "Vasily Podkolzin"]
OilersDef1 = ["Evan Bouchard", "Mattias Ekholm", "Darnell Nurse", "Jake Walman", "Brett Kulak", "Ty Emberson", "John Klingberg", "Troy Stecher"]
OilersDef2 = ["Evan Bouchard", "Mattias Ekholm", "Darnell Nurse", "Jake Walman", "Brett Kulak", "Ty Emberson", "John Klingberg", "Troy Stecher"]
OilersG = ["Stuart Skinner", "Calvin Pickard"]

#Panthers
PanthersC = ["Aleksander Barkov", "Sam Bennett", "Jesper Boqvist", "Anton Lundell", "Eetu Luostarinen", "Sam Reinhart", "Evan Rodrigues", "Carter Verhaeghe", "Nico Sturm", "Brad Marchand"]
PanthersLW = ["Matthew Tkachuk", "Jonah Gadjovich", "A.J. Greer", "Tomas Nosek"]
PanthersRW = ["Makie Samoskevich"]
PanthersDef1 = ["Nate Schmidt", "Gustav Forsling", "Seth Jones", "Dmitry Kulikov", "Uvis Balinskis", "Niko Mikkola"]
PanthersDef2 = ["Nate Schmidt", "Gustav Forsling", "Seth Jones", "Dmitry Kulikov", "Uvis Balinskis", "Niko Mikkola"]
PanthersG = ["Sergei Bobrovsky","Vitek Vanecek"]

#Kings
KingsC = ["Anze Kopitar", "Phillip Danault", "Samuel Helenius", "Trevor Lewis", "Akil Thomas", "Alex Turcotte"]
KingsLW = ["Kevin Fiala", "Warren Foegele", "Tanner Jeannot", "Andrei Kuzmenko", "Andre Lee", "Trevor Moore"]
KingsRW = ["Adrian Kempe", "Alex Laferriere", "Quinton Byfield"]
KingsDef1 = ["Mikey Anderson", "Joel Edmundson", "Jacob Moverare", "Drew Doughty", "Vladislav Gavrikov", "Jordan Spence", "Kyle Burroughs", "Brandt Clarke"]
KingsDef2 = ["Mikey Anderson", "Joel Edmundson", "Jacob Moverare", "Drew Doughty", "Vladislav Gavrikov", "Jordan Spence", "Kyle Burroughs", "Brandt Clarke"]
KingsG = ["Darcy Kuemper", "David Rittich"]

#Wild
WildC = ["Joel Eriksson Ek", "Frederick Gaudreau", "Brendan Gaunce", "Vinnie Hinostroza", "Gustav Nyquist", "Marco Rossi", "Devin Shore", "Yakov Trenin"]
WildLW = ["Matt Boldy", "Kirill Kaprizov", "Marcus Johansson", "Marcus Foligno"]
WildRW = ["Ryan Hartman", "Mats Zuccarello", "Justin Brazeau"]
WildDef1 = ["Jonas Brodin", "Declan Chisholm", "Brock Faber", "Jon Merrill", "Jacob Middleton", "Jared Spurgeon", "Zach Bogosian", "David Jiricek"]
WildDef2 = ["Jonas Brodin", "Declan Chisholm", "Brock Faber", "Jon Merrill", "Jacob Middleton", "Jared Spurgeon", "Zach Bogosian", "David Jiricek"]
WildG = ["Marc-Andre Fleury", "Filip Gustavsson"]

#Canadiens
CanadiensC = ["Nick Suzuki", "Kirby Dach", "Alex Newhook", "Christian Dvorak", "Jake Evans"]
CanadiensLW = ["Emil Heineman", "Michael Pezzetta", "Juraj Slafkovsky"]
CanadiensRW = ["Josh Anderson", "Joel Armia", "Brendan Gallagher", "Patrik Laine", "Joshua Roy", "Cole Caufield"]
CanadiensDef1 = ["Kaiden Guhle", "David Savard", "Arber Xhekaj", "Lane Hutson", "Alexandre Carrier" "Mike Matheson", "Jayden Struble"]
CanadiensDef2 = ["Kaiden Guhle", "David Savard", "Arber Xhekaj", "Lane Hutson", "Alexandre Carrier" "Mike Matheson", "Jayden Struble"]
CanadiensG = ["Sam Montembeault", "Jakub Dobes"]

#Predators
PredatorsC = ["Steven Stamkos", "Jyan O'Reilly", "Colton Sissons" "Jonathan Marchessault", "Fedor Svechkov"]
PredatorsLW = ["Michael Bunting", "Filip Forsberg", "Zachary L'Heureux", "Kieffer Bellows", "Cole Smith", "Jakub Vrana"]
PredatorsRW = ["Luke Evangelista", "Michael McCarron"]
PredatorsDef1 = ["Roman Josi", "Brady Skjei", "Jeremy Lauzon", "Andreas Englund", "Adam Wilsby", "Nick Blankenburg", "Justin Barron", "Jordan Oesterle", "Spencer Stastney", "Marc Del Gaizo"]
PredatorsDef2 = ["Roman Josi", "Brady Skjei", "Jeremy Lauzon", "Andreas Englund", "Adam Wilsby", "Nick Blankenburg", "Justin Barron", "Jordan Oesterle", "Spencer Stastney", "Marc Del Gaizo"]
PredatorsG = ["Juuse Saros", "Justus Annunen"]

#Devils
DevilsC = ["Nico Hischier", "Jack Hughes", "Dawson Mercer", "Paul Cotter", "Johan Larsson", "Justin Dowling", "Cody Glass"]
DevilsLW = ["Jesper Bratt", "Ondrej Palat", "Tomas Tatar", "Kurtis MacDermid", "Erik Haula"]
DevilsRW = ["Timo Meier", "Stefan Noesen", "Nathan Bastian", "Daniel Sprong"]
DevilsDef1 = ["Dougie Hamilton", "Jonas Siegenthaler", "Brenden Dillon", "Brett Pesce", "Luke Hughes", "Johnathan Kovacevic", "Dennis Cholowski", "Brian Dumoulin", "Simon Nemec"]
DevilsDef2 = ["Dougie Hamilton", "Jonas Siegenthaler", "Brenden Dillon", "Brett Pesce", "Luke Hughes", "Johnathan Kovacevic", "Dennis Cholowski", "Brian Dumoulin", "Simon Nemec"]
DevilsG = ["Jacob Markstrom", "Jake Allen"]

#Islanders
IslandersC = ["Mathew Barzal", "Casey Cizikas", "Marc Gatcomb", "Bo Horvat", "Kyle MacLean", "Kyle Palmieri", "Jean-Gabriel Pageau"]
IslandersLW = ["Anthony Duclair", "Pierre Engvall", "Anders Lee", "Matt Martin"]
IslandersRW = ["Hudson Fasching", "Simon Holmstrom", "Maxim Tsyplakov"]
IslandersDef1 = ["Adam Pelech", "Alexander Romanov", "Ryan Pulock", "Noah Dobson", "Scott Perunovich", "Adam Boqvist", "Tony DeAngelo", "Scott Mayfield", "Mike Reilly"]
IslandersDef2 = ["Adam Pelech", "Alexander Romanov", "Ryan Pulock", "Noah Dobson", "Scott Perunovich", "Adam Boqvist", "Tony DeAngelo", "Scott Mayfield", "Mike Reilly"]
IslandersG = ["Ilya Sorokin", "Semyon Varlamov", "Marcus Hogberg"]

#Rangers
RangersC = ["Mika Zibanejad", "Vincent Trocheck", "Sam Carrick", "Jonny Brodzinski", "Juuso Parssinen", "Matt Rempe", "Adam Edstrom"]
RangersLW = ["Chris Kreider", "Will Cuylle", "Brett Berard", "JT Miller", "Alexis Lafreniere", "Artemi Panarin", "Brennan Othmann"]
RangersRW = ["Arthur Kaliyev"]
RangersDef1 = ["Carson Saucy", "K'Andre Miller", "Zac Jones", "Adam Fox", "Calvin de Haan", "Will Borgen", "Braden Schneider", "Urho Vaakanainen"]
RangersDef2 = ["Carson Saucy", "K'Andre Miller", "Zac Jones", "Adam Fox", "Calvin de Haan", "Will Borgen", "Braden Schneider", "Urho Vaakanainen"]
RangersG = ["Igor Shesterkin", "Jonathan Quick"]

#Senators
SenatorsC = ["Tim Stützle", "Dylan Cozens", "Shane Pinto", "Ridly Greig", "Nick Cousins", "Matthew Highmore"]
SenatorsLW = ["Brady Tkachuk", "Fabian Zetterlund", "David Perron"]
SenatorsRW = ["Drake Batherson", "Claude Giroux", "Adam Gaudette", "Michael Amadio"]
SenatorsDef1 = ["Thomas Chabot", "Jake Sanderson", "Tyler Kleven", "Nick Jensen", "Travis Hamonic", "Dennis Gilbert", "Nikolas Matinpalo", "Artem Zub"]
SenatorsDef2 = ["Thomas Chabot", "Jake Sanderson", "Tyler Kleven", "Nick Jensen", "Travis Hamonic", "Dennis Gilbert", "Nikolas Matinpalo", "Artem Zub"]
SenatorsG = ["Linus Ullmark", "Anton Forsberg", "Leevi Merilainen"]

# Flyers
FlyersC = ["Sean Couturier", "Ryan Poehling", "Rodrigo Abols"]
FlyersLW = ["Jakob Pelletier", "Nicolas Deslauriers", "Noah Cates"]
FlyersRW = ["Tyson Foerster", "Travis Konecny", "Bobby Brink", "Olle Lycksell", "Garnet Hathaway", "Matvei Michkov", "Owen Tippet"]
FlyersDef1 = ["Jamie Drysdale", "Emil Andrae", "Rasmus Ristolainen", "Travis Sanheim", "Nick Seeler", "Cam York", "Egor Zamula", "Ryan Ellis"]
FlyersDef2 = ["Jamie Drysdale", "Emil Andrae", "Rasmus Ristolainen", "Travis Sanheim", "Nick Seeler", "Cam York", "Egor Zamula", "Ryan Ellis"]
FlyersG = ["Samuel Ersson", "Ivan Fedotov"]

#Penguins
PenguinsC = ["Sidney Crosby", "Evgeni Malkin", "Emil Bemstrom", "Philip Tomasino", "Noel Acciari", "Tommy Novak", "Connor Dewar", "Blake Lizotte"]
PenguinsLW = ["Matt Nieto", "Bokondji Imama", "Danton Heinen"]
PenguinsRW = ["Rickard Rakell", "Bryan Rust", "Kevin Hayes"]
PenguinsDef1 = ["Ryan Graves", "Matt Grzelcyk", "Pierre-Olivier Joseph", "Ryan Shea", "Kris Letang", "Erik Karlsson", "Sebastian Aho", "Vadislav Kolyachonok", "Conor Timmins"]
PenguinsDef2 = ["Ryan Graves", "Matt Grzelcyk", "Pierre-Olivier Joseph", "Ryan Shea", "Kris Letang", "Erik Karlsson", "Sebastian Aho", "Vadislav Kolyachonok", "Conor Timmins"]
PenguinsG = ["Tristan Jarry", "Alex Nedeljkovic"]

#Sharks
SharksC = ["Macklin Celebrini", "Logan Couture", "Ty Dellandrea", "Noah Gregor", "Klim Kostin", "Will Smith", "Tyler Toffoli", "Alexander Wennberg"]
SharksLW = ["William Eklund"]
SharksRW = ["Patrick Giles", "Barclay Goodrow", "Collin Graf", "Carl Grundstrom", "Nikolai Kovalenko"]
SharksDef1 = ["Mario Ferraro", "Marc-Edouard Vlasic", "Timothy Liljegren", "Jan Rutta", "Shakir Mukhamadullin", "Henry Thrun", "Vincent Desharnais", "Jimmy Schuldt"]
SharksDef2 = ["Mario Ferraro", "Marc-Edouard Vlasic", "Nikita Okhotiuk", "Jan Rutta", "Matt Benning", "Henry Thrun", "Vincent Desharnais"]
SharksG = ["Alexandar Georgiev", "Georgi Romanov"]

#Kraken
KrakenC = ["Matty Beniers", "Chandler Stephenson", "Jaden Schwartz", "John Hayden", "Michael Eyssimont", "Shane Wright"]
KrakenLW = ["Jared McCann", "Tye Kartye", "Andre Burakovsky"]
KrakenRW = ["Jordan Eberle", "Jani Nyman", "Kaapo Kakko", "Eeli Tolvanen"]
KrakenDef1 = ["Vince Dunn", "Jamie Oleksiak", "Ryker Evans", "Adam Larsson", "Joshua Mahura", "Cale Fleury", "Brandon Montour"]
KrakenDef2 = ["Vince Dunn", "Jamie Oleksiak", "Ryker Evans", "Adam Larsson", "Joshua Mahura", "Cale Fleury", "Brandon Montour"]
KrakenG = ["Philipp Grubauer", "Joey Daccord"]

#Blues
BluesC = ["Jordan Kyrou", "Brayden Schenn", "Robert Thomas", "Radek Faksa", "Oskar Sundqvist", "Zack Bolduc", "Alexandre Texier", "Dylan Holloway"]
BluesLW = ["Pavel Buchnevich", "Nathan Walker", "Jake Neighbours"]
BluesRW = ["Alexei Toropchenko", "Mathieu Joseph"]
BluesDef1 = ["Nick Leddy", "Ryan Suter", "Scott Perunovich", "Tyler Tucker", "Colton Parayko", "Justin Faulk", "Cam Fowler", "Philip Broberg"]
BluesDef2 = ["Nick Leddy", "Ryan Suter", "Scott Perunovich", "Tyler Tucker", "Colton Parayko", "Justin Faulk", "Cam Fowler", "Philip Broberg"]
BluesG = ["Jordan Binnington", "Joel Hofer"]

#Lightning
LightningC = ["Anthony Cirelli", "Zemgus Girgensons", "Luke Glendening", "Brayden Point", "Jake Guentzel", "Yanni Gourde", "Gage Gonclaves"]
LightningLW = ["Brandon Hagel", "Brandon Hagel"]
LightningRW = ["Oliver Bjorkstrand", "Mitchell Chaffee", "Nikita Kucherov"]
LightningDef1 = ["Victor Hedman", "Erik Cernak", "Darren Raddysh", "Emil Lilleberg", "Ryan McDonagh", "J.J. Moser", "Nick Perbix"]
LightningDef2 = ["Victor Hedman", "Erik Cernak", "Darren Raddysh", "Emil Lilleberg", "Ryan McDonagh", "J.J. Moser", "Nick Perbix"]
LightningG = ["Andrei Vasilevskiy", "Jonas Johansson"]

#Maple_Leafs
Maple_LeafsC = ["Auston Matthews", "John Tavares", "Max Domi", "David Kampf", "Calle Jarnkrok", "Steven Lorentz", "Bobby McMann"]
Maple_LeafsLW = ["Nicholas Robertson", "Matthew Knies", "Scott Laughton", "Max Pacioretty"]
Maple_LeafsRW = ["William Nylander", "Mitch Marner", "Pontus Holmberg"]
Maple_LeafsDef1 = ["Morgan Rielly", "Jake McCabe", "Simon Benoit", "Oliver Ekman-Larsson", "Chris Tanev", "Jani Hakanpaa", "Brendon Carlo", "Philippe Myers"]
Maple_LeafsDef2 = ["Morgan Rielly", "Jake McCabe", "Simon Benoit", "Oliver Ekman-Larsson", "Chris Tanev", "Jani Hakanpaa", "Brendon Carlo", "Philippe Myers"]
Maple_LeafsG = ["Anthony Stolarz", "Joseph Woll"]

#Hockey_Club
Hockey_ClubC = ["Clayton Keller", "Logan Cooley", "Jack McBain", "Barrett Hayton" "Alexander Kerfoot", "Kevin Stenlund", "Nick Schmaltz", "Liam O'Brien", "Nick Bjugstad"]
Hockey_ClubLW = ["Lawson Crouse", "Matias Maccelli", "Michael Carcone"]
Hockey_ClubRW = ["Dylan Guenther", "Josh Doan"]
Hockey_ClubDef1 = ["Mikhail Sergachev", "Ian Cole", "Michael Kesselring", "Olli Maata", "John Marino", "Robert Bortuzzo", "Nick DeSimone"]
Hockey_ClubDef2 = ["Mikhail Sergachev", "Ian Cole", "Michael Kesselring", "Olli Maata", "John Marino", "Robert Bortuzzo", "Nick DeSimone"]
Hockey_ClubG = ["Karel Vejmelka", "Jaxson Stauber"]

#Canucks
CanucksC = ["Elias Pettersson", "Filip Chytil", "Pius Suter", "Nils Aman", "Teddy Blueger", "Dakota Joshua"]
CanucksLW = ["Jake DeBrusk", "Nils Hoglander", "Kiefer Sherwood", "Drew O'Connor"]
CanucksRW = ["Brock Boeser", "Jonathan Lekkerimaki", "Conor Garland"]
CanucksDef1 = ["Elias Pettersson", "Quinn Hughes", "Derek Forbort", "Marcus Pettersson", "Victor Mancini", "Tyler Myers", "Filip Hronek", "Noah Juulsen"]
CanucksDef2 = ["Elias Pettersson", "Quinn Hughes", "Derek Forbort", "Marcus Pettersson", "Victor Mancini", "Tyler Myers", "Filip Hronek", "Noah Juulsen"]
CanucksG = ["Thatcher Demko", "Arturs Silovs", "Kevin Lankinen"]

#Golden_Knights
Golden_KnightsC = ["Ivan Barbashev", "Jack Eichel", "Tomas Hertl", "Brett Howden", "William Karlsson", "Rafael Lavoie", "Nicolas Roy"]
Golden_KnightsLW = ["Pavel Dorofeyev", "Brandon Saad", "Tanner Pearson"]
Golden_KnightsRW = ["Jonas Rondbjerg", "Keegan Kolesar", "Victor Olofsson", "Mark Stone", "Cole Schwindt", "Reilly Smith"]
Golden_KnightsDef1 = ["Shea Theodore", "Noah Hanifin", "Nicolas Hague", "Brayden McNabb", "Ben Hutton", "Alex Pietrangelo", "Zach Whitecloud", "Kaedan Korczak"]
Golden_KnightsDef2 = ["Shea Theodore", "Noah Hanifin", "Nicolas Hague", "Brayden McNabb", "Ben Hutton", "Alex Pietrangelo", "Zach Whitecloud", "Kaedan Korczak"]
Golden_KnightsG = ["Adin Hill", "Ilya Samsonov"]

#Capitals
CapitalsC = [ "Nic Dowd", "Lars Eller", "Nicklas Backstrom", "Connor McMichael", "Dylan Strome", "Ethen Frank", "Aliaksei Protas"]
CapitalsLW = ["Alex Ovechkin", "Anthony Beauvillier", "Andrew Mangiapane", "Pierre-Luc Dubois", "Sonny Milano"]
CapitalsRW = ["Taylor Raddysh", "T.J. Oshie", "Tom Wilson", "Brandon Duhaime"]
CapitalsDef1 = ["Jakob Chychrun", "Rasmus Sandin", "Martin Fehervary", "Matt Roy", "John Carlson", "Trevor van Riemsdyk", "Dylan Mcllrath", "Alexander Alexeyev"]
CapitalsDef2 = ["Jakob Chychrun", "Rasmus Sandin", "Martin Fehervary", "Matt Roy", "John Carlson", "Trevor van Riemsdyk", "Dylan Mcllrath", "Alexander Alexeyev"]
CapitalsG = ["Charlie Lindgren", "Logan Thompson"]

#Jets
JetsC = ["Mason Appleton", "Morgan Barron", "David Gustafsson", "Rasmus Kupari", "Adam Lowry", "Vladislav Namestnikov", "Cole Perfetti", "Mark Scheifele", "Gabriel Vilardi"]
JetsLW = ["Kyle Connor", "Nikolaj Ehlers", "Alex Iafallo", "Brandon Tanev"]
JetsRW = ["Nino Niederreiter"]
JetsDef1 = ["Dylan DeMelo", "Dylan Samberg", "Haydn Fleury", "Ville Heinola", "Josh Morrissey", "Neal Pionk", "Colin Miller", "Logan Stanley", "Luke Schenn"]
JetsDef2 = ["Dylan DeMelo", "Dylan Samberg", "Haydn Fleury", "Ville Heinola", "Josh Morrissey", "Neal Pionk", "Colin Miller", "Logan Stanley", "Luke Schenn"]
JetsG = ["Connor Hellebuyck", "Eric Comrie"]
