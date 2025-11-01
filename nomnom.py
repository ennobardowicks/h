# ================================
# 🛠️ Konfiguration & Konstanten
# ================================

APP_NAME = "NomNom"
ICON = "🍽️"

# Standard-Haltbarkeitsdauer (in Tagen)
DEFAULT_HALTBARKEIT = {
    "Milch": 7, "Eier": 21, "Butter": 21, "Hähnchenbrust": 2,
    "Gurke": 5, "Tomaten": 4, "Zucchini": 5, "Kartoffeln": 14,
    "Apfel": 10, "Banane": 5, "Brot": 5, "Käse": 10,
    "Joghurt": 7, "Eis": 30, "Pasta": 12, "Reis": 12,
    "Zucker": 365, "Salz": 365, "Öl": 365, "Honig": 365,
    "Kartoffel": 14, "Zwiebel": 14, "Paprika": 7, "Spinat": 3,
    "Rucola": 2, "Petersilie": 5, "Koriander": 5, "Lemon": 7,
    "Orange": 10, "Ananas": 5, "Trauben": 7, "Erdbeeren": 3,
    "Kirschen": 3, "Pflaumen": 5, "Blaubeeren": 5, "Heidelbeeren": 5,
    "Schinken": 5, "Wurst": 5, "Räucherlachs": 7, "Lachs": 2,
    "Tofu": 3, "Tempeh": 5, "Mungobohnenkeimlinge": 3,
    "Kokosmilch": 7, "Sojasauce": 365, "Senf": 365, "Mayonnaise": 30,
    "Pesto": 14, "Ketchup": 180, "Marmelade": 180, "Honig": 365,
    "Kakao": 365, "Kaffeebohnen": 180, "Tee": 180, "Nüsse": 90,
    "Mandeln": 90, "Walnüsse": 90, "Haselnüsse": 90, "Pistazien": 90,
    "Chia-Samen": 180, "Leinsamen": 180, "Kürbiskerne": 180,
    "Kokosnuss": 14, "Ananas": 5, "Papaya": 5, "Mango": 5,
    "Kiwi": 7, "Pfirsich": 5, "Nektarine": 5, "Marille": 5,
    "Datteln": 180, "Rosinen": 180, "Süßkartoffel": 14,
    "Zimt": 365, "Pfeffer": 365, "Kurkuma": 365, "Kardamom": 365,
    "Ingwer": 7, "Knoblauch": 14, "Lauch": 7, "Rettich": 7,
    "Radieschen": 7, "Rucola": 2, "Basilikum": 5, "Petersilie": 5,
    "Dill": 5, "Schnittlauch": 5, "Thymian": 365, "Oregano": 365,
    "Rosmarin": 365, "Schnittknoblauch": 7, "Zitronengras": 7,
    "Chili": 7, "Paprikapulver": 365, "Kurkumapulver": 365,
    "Sesam": 365, "Tahini": 90, "Mandelmus": 90, "Haselnussmus": 90,
    "Kokosnussmus": 90, "Peanutbutter": 180, "Nussmus": 90,
    "Kokosraspeln": 180, "Zucker": 365, "Honig": 365, "Ahornsirup": 365,
    "Balsamico": 365, "Weißwein": 30, "Rotwein": 30, "Sekt": 30,
    "Bier": 30, "Wodka": 365, "Whisky": 365, "Rum": 365,
    "Gin": 365, "Tequila": 365, "Cognac": 365, "Schnaps": 365,
    "Likör": 365, "Eis": 30, "Schokolade": 120, "Kekse": 30,
    "Muffins": 5, "Kuchen": 3, "Pfannkuchen": 2, "Waffeln": 5,
    "Biskuits": 30, "Nuggets": 2, "Frikadellen": 2, "Fischfilet": 2,
    "Sardinen": 5, "Hering": 5, "Sardellen": 5, "Sardellenpaste": 365,
    "Sardellenöl": 365, "Sardellensoße": 30, "Sardellenfilet": 5,
}

# Rezepte (nach Lebensmittel)
REZEPTE = {
    "Milch": [
        "Milchpudding: 200ml Milch, 2 EL Zucker, 1 Ei, 1 TL Vanille, 1 EL Mehl. 10 min kochen, abkühlen lassen.",
        "Milchshake: Milch, Vanilleeis, Schokolade, 1 TL Zucker. Mixen.",
        "Pancakes: 150g Mehl, 1 Ei, 200ml Milch, 1 TL Backpulver, 1 TL Zucker. 2 min pro Seite backen."
    ],
    "Eier": [
        "Omelett: 2 Eier, Salz, Pfeffer, etwas Butter. In Pfanne braten.",
        "Eierkuchen: 2 Eier, 100ml Milch, 50g Mehl, 1 TL Zucker. 3 min pro Seite backen.",
        "Hühnerfrikassee: 2 Eier, 200g Hähnchenbrust, 1 Zwiebel, 100ml Sahne, 1 TL Curry."
    ],
    "Gurke": [
        "Gurkensalat: Gurke, Zwiebel, Essig, Öl, Salz, Pfeffer, Dill.",
        "Gurkensuppe: Gurke, Zwiebel, Knoblauch, Gemüsebrühe, Sahne, Dill.",
        "Gurkensalat mit Joghurt: Gurke, Joghurt, Zwiebel, Dill, Salz, Pfeffer."
    ],
    "Tomaten": [
        "Tomatensalat: Tomaten, Zwiebel, Basilikum, Olivenöl, Balsamico.",
        "Tomatensuppe: Tomaten, Zwiebel, Knoblauch, Gemüsebrühe, Kräuter.",
        "Panini mit Tomaten: Brot, Tomaten, Mozzarella, Basilikum, Olivenöl."
    ],
    "Zucchini": [
        "Zucchini-Pfannkuchen: Zucchini, Mehl, Ei, Salz, Pfeffer, 2 min pro Seite.",
        "Zucchiniblüten: Zucchini-Blüten mit Teig füllen, frittieren.",
        "Zucchini-Nudeln: Zucchini mit Spiralizer, mit Tomatensauce."
    ],
    "Kartoffeln": [
        "Kartoffelsalat: Kartoffeln, Zwiebel, Gurke, Essig, Öl, Senf, Dill.",
        "Kartoffelpuffer: Kartoffeln, Mehl, Ei, Zwiebel, Salz, Pfeffer, frittieren.",
        "Ofenkartoffeln: Kartoffeln mit Salz, Pfeffer, Öl, Rosmarin, 45 min backen."
    ],
    "Brot": [
        "Toast: Brot, Butter, Marmelade, Honig.",
        "Brotzeit: Brot, Käse, Wurst, Gurke, Zwiebel.",
        "Brotcroutons: Brot, Öl, Knoblauch, Salz, 15 min backen."
    ],
    "Käse": [
        "Käseplatte: Käse, Brot, Obst, Nüsse, Honig.",
        "Käsespätzle: Käse, Spätzle, Sahne, Butter, Pfeffer.",
        "Käsesuppe: Käse, Milch, Kartoffeln, Zwiebel, Kräuter."
    ],
    "Hähnchenbrust": [
        "Hähnchenbrust mit Kartoffeln: Hähnchenbrust, Kartoffeln, Zwiebel, Knoblauch, Salz, Pfeffer.",
        "Hähnchen-Curry: Hähnchenbrust, Curry, Kokosmilch, Zwiebel, Knoblauch.",
        "Hähnchen-Salat: Hähnchenbrust, Salat, Tomaten, Gurke, Joghurt-Dressing."
    ],
    "Joghurt": [
        "Joghurt mit Obst: Joghurt, Beeren, Honig, Nüsse.",
        "Joghurt-Smoothie: Joghurt, Banane, Erdbeeren, Honig.",
        "Joghurt-Dressing: Joghurt, Zwiebel, Dill, Essig, Öl."
    ],
    "Erdbeeren": [
        "Erdbeeren mit Schokolade: Erdbeeren, Schokolade, Sahne.",
        "Erdbeersmoothie: Erdbeeren, Joghurt, Milch, Honig.",
        "Erdbeerkuchen: Erdbeeren, Mürbeteig, Butter, Zucker."
    ],
    "Apfel": [
        "Apfelkuchen: Apfel, Mehl, Zucker, Butter, Zimt.",
        "Apfelschorle: Apfel, Wasser, Zitrone, Zucker.",
        "Apfelstrudel: Apfel, Zimt, Zucker, Mürbeteig, Butter."
    ],
    "Zucker": [
        "Zuckerwatte: Zucker, Wasser, Farbe, Stäbchen.",
        "Zucker-Sirup: Zucker, Wasser, Zitrone, Zimt.",
        "Zucker-Karamell: Zucker, Wasser, Butter, Sahne."
    ],
    "Honig": [
        "Honig-Tea: Honig, Zitrone, Wasser, Ingwer.",
        "Honig-Brot: Honig, Brot, Butter.",
        "Honig-Dressing: Honig, Essig, Öl, Senf."
    ],
    "Pasta": [
        "Pasta mit Tomatensauce: Pasta, Tomaten, Zwiebel, Knoblauch, Basilikum.",
        "Pasta mit Käse: Pasta, Käse, Sahne, Butter, Pfeffer.",
        "Pasta mit Gemüse: Pasta, Zucchini, Paprika, Zwiebel, Knoblauch."
    ],
    "Reis": [
        "Reis mit Gemüse: Reis, Zucchini, Paprika, Zwiebel, Knoblauch.",
        "Reis mit Hähnchen: Reis, Hähnchenbrust, Zwiebel, Knoblauch, Sojasauce.",
        "Reis mit Fisch: Reis, Fischfilet, Zitrone, Kräuter."
    ],
    "Kokosmilch": [
        "Kokoscurry: Kokosmilch, Curry, Hähnchen, Zwiebel, Knoblauch.",
        "Kokosreis: Kokosmilch, Reis, Zimt, Zucker.",
        "Kokos-Smoothie: Kokosmilch, Banane, Erdbeeren, Honig."
    ],
    "Bananen": [
        "Bananenmuffins: Banane, Mehl, Ei, Zucker, Milch, Backpulver.",
        "Bananen-Smoothie: Banane, Joghurt, Milch, Honig.",
        "Bananenbrot: Banane, Mehl, Ei, Zucker, Butter, Zimt."
    ],
    "Eis": [
        "Eiscreme: Milch, Sahne, Zucker, Ei, Vanille.",
        "Eis mit Obst: Eis, Beeren, Schokolade.",
        "Eis-Torte: Eis, Kekse, Sahne, Schokolade."
    ],
    "Schokolade": [
        "Schokoladenkuchen: Schokolade, Mehl, Ei, Zucker, Butter.",
        "Schokoladenmousse: Schokolade, Sahne, Ei, Zucker.",
        "Schokoladen-Smoothie: Schokolade, Milch, Banane, Honig."
    ],
    "Nüsse": [
        "Nussmischung: Nüsse, Honig, Zimt, Salz.",
        "Nussbutter: Nüsse, Öl, Salz, Honig.",
        "Nuss-Salat: Nüsse, Salat, Apfel, Zwiebel, Dressing."
    ],
    "Kokosnuss": [
        "Kokosreis: Kokosmilch, Reis, Zimt, Zucker.",
        "Kokos-Salat: Kokosnuss, Salat, Tomaten, Zwiebel.",
        "Kokos-Curry: Kokosmilch, Curry, Hähnchen, Zwiebel, Knoblauch."
    ],
    "Kartoffel": [
        "Kartoffelpuffer: Kartoffeln, Mehl, Ei, Zwiebel, Salz, Pfeffer.",
        "Kartoffelsalat: Kartoffeln, Zwiebel, Gurke, Essig, Öl, Dill.",
        "Ofenkartoffeln: Kartoffeln, Salz, Pfeffer, Öl, Rosmarin."
    ],
    "Zwiebel": [
        "Zwiebelkuchen: Zwiebel, Mehl, Ei, Milch, Butter.",
        "Zwiebelsoße: Zwiebel, Sahne, Butter, Pfeffer.",
        "Zwiebelbratlinge: Zwiebel, Mehl, Ei, Salz, Pfeffer, frittieren."
    ],
    "Paprika": [
        "Paprikasalat: Paprika, Zwiebel, Gurke, Essig, Öl, Dill.",
        "Paprikasuppe: Paprika, Zwiebel, Knoblauch, Gemüsebrühe.",
        "Paprikapfannkuchen: Paprika, Mehl, Ei, Milch, Salz, Pfeffer."
    ],
    "Spinat": [
        "Spinat-Omelett: Spinat, Ei, Butter, Salz, Pfeffer.",
        "Spinat-Pasta: Spinat, Pasta, Knoblauch, Öl, Parmesan.",
        "Spinat-Suppe: Spinat, Zwiebel, Kartoffeln, Gemüsebrühe."
    ],
    "Rucola": [
        "Rucola-Salat: Rucola, Tomaten, Ziegenkäse, Olivenöl, Balsamico.",
        "Rucola-Pasta: Rucola, Pasta, Parmesan, Olivenöl, Zitrone.",
        "Rucola-Sandwich: Rucola, Tomaten, Käse, Brot."
    ],
    "Petersilie": [
        "Petersiliensoße: Petersilie, Joghurt, Zwiebel, Essig, Öl.",
        "Petersilien-Pesto: Petersilie, Knoblauch, Nüsse, Öl, Parmesan.",
        "Petersilien-Topping: Petersilie, Zitrone, Öl, Salz, Pfeffer."
    ],
    "Koriander": [
        "Koriander-Salat: Koriander, Tomaten, Gurke, Zwiebel, Zitrone.",
        "Koriander-Curry: Koriander, Hähnchen, Curry, Kokosmilch.",
        "Koriander-Dressing: Koriander, Joghurt, Zitrone, Öl, Salz."
    ],
    "Lemon": [
        "Zitronenwasser: Zitrone, Wasser, Honig.",
        "Zitronen-Kuchen: Zitrone, Mehl, Ei, Zucker, Butter.",
        "Zitronen-Dressing: Zitrone, Öl, Senf, Honig, Salz."
    ],
    "Orange": [
        "Orangensaft: Orange, Wasser, Honig.",
        "Orangen-Salat: Orange, Rucola, Nüsse, Honig.",
        "Orangen-Creme: Orange, Sahne, Zucker, Vanille."
    ],
    "Ananas": [
        "Ananas-Salat: Ananas, Gurke, Zwiebel, Zitrone, Dill.",
        "Ananas-Smoothie: Ananas, Joghurt, Milch, Honig.",
        "Ananas-Kuchen: Ananas, Mehl, Ei, Zucker, Butter."
    ],
    "Papaya": [
        "Papaya-Salat: Papaya, Gurke, Zwiebel, Zitrone, Dill.",
        "Papaya-Smoothie: Papaya, Joghurt, Milch, Honig.",
        "Papaya-Kuchen: Papaya, Mehl, Ei, Zucker, Butter."
    ],
    "Mango": [
        "Mango-Salat: Mango, Gurke, Zwiebel, Zitrone, Dill.",
        "Mango-Smoothie: Mango, Joghurt, Milch, Honig.",
        "Mango-Kuchen: Mango, Mehl, Ei, Zucker, Butter."
    ],
    "Kiwi": [
        "Kiwi-Salat: Kiwi, Apfel, Zwiebel, Zitrone, Honig.",
        "Kiwi-Smoothie: Kiwi, Joghurt, Milch, Honig.",
        "Kiwi-Kuchen: Kiwi, Mehl, Ei, Zucker, Butter."
    ],
    "Pfirsich": [
        "Pfirsich-Salat: Pfirsich, Gurke, Zwiebel, Zitrone, Honig.",
        "Pfirsich-Smoothie: Pfirsich, Joghurt, Milch, Honig.",
        "Pfirsich-Kuchen: Pfirsich, Mehl, Ei, Zucker, Butter."
    ],
    "Nektarine": [
        "Nektarine-Salat: Nektarine, Gurke, Zwiebel, Zitrone, Honig.",
        "Nektarine-Smoothie: Nektarine, Joghurt, Milch, Honig.",
        "Nektarine-Kuchen: Nektarine, Mehl, Ei, Zucker, Butter."
    ],
    "Marille": [
        "Marille-Salat: Marille, Gurke, Zwiebel, Zitrone, Honig.",
        "Marille-Smoothie: Marille, Joghurt, Milch, Honig.",
        "Marille-Kuchen: Marille, Mehl, Ei, Zucker, Butter."
    ],
    "Datteln": [
        "Dattel-Salat: Datteln, Nüsse, Salat, Honig.",
        "Dattel-Smoothie: Datteln, Joghurt, Milch, Honig.",
        "Dattel-Kuchen: Datteln, Mehl, Ei, Zucker, Butter."
    ],
    "Rosinen": [
        "Rosinen-Salat: Rosinen, Nüsse, Salat, Honig.",
        "Rosinen-Smoothie: Rosinen, Joghurt, Milch, Honig.",
        "Rosinen-Kuchen: Rosinen, Mehl, Ei, Zucker, Butter."
    ],
    "Süßkartoffel": [
        "Süßkartoffel-Puffer: Süßkartoffel, Mehl, Ei, Salz, Pfeffer.",
        "Süßkartoffel-Ofen: Süßkartoffel, Öl, Salz, Pfeffer, Zimt.",
        "Süßkartoffel-Salat: Süßkartoffel, Apfel, Zwiebel, Dressing."
    ],
    "Zimt": [
        "Zimt-Tea: Zimt, Wasser, Honig.",
        "Zimt-Kuchen: Zimt, Mehl, Ei, Zucker, Butter.",
        "Zimt-Smoothie: Zimt, Joghurt, Milch, Honig."
    ],
    "Pfeffer": [
        "Pfeffer-Salat: Pfeffer, Tomaten, Gurke, Zwiebel, Öl.",
        "Pfeffer-Suppe: Pfeffer, Zwiebel, Kartoffeln, Gemüsebrühe.",
        "Pfeffer-Pasta: Pfeffer, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Kurkuma": [
        "Kurkuma-Tee: Kurkuma, Wasser, Honig, Zitrone.",
        "Kurkuma-Curry: Kurkuma, Hähnchen, Kokosmilch, Zwiebel, Knoblauch.",
        "Kurkuma-Smoothie: Kurkuma, Joghurt, Milch, Honig."
    ],
    "Kardamom": [
        "Kardamom-Tee: Kardamom, Wasser, Honig.",
        "Kardamom-Kuchen: Kardamom, Mehl, Ei, Zucker, Butter.",
        "Kardamom-Smoothie: Kardamom, Joghurt, Milch, Honig."
    ],
    "Ingwer": [
        "Ingwer-Tee: Ingwer, Wasser, Honig, Zitrone.",
        "Ingwer-Curry: Ingwer, Hähnchen, Kokosmilch, Zwiebel, Knoblauch.",
        "Ingwer-Smoothie: Ingwer, Joghurt, Milch, Honig."
    ],
    "Knoblauch": [
        "Knoblauchbrot: Knoblauch, Brot, Butter.",
        "Knoblauch-Sauce: Knoblauch, Joghurt, Zwiebel, Essig, Öl.",
        "Knoblauch-Pasta: Knoblauch, Pasta, Öl, Parmesan."
    ],
    "Lauch": [
        "Lauchsuppe: Lauch, Kartoffeln, Gemüsebrühe, Sahne.",
        "Lauch-Pfannkuchen: Lauch, Mehl, Ei, Milch, Salz, Pfeffer.",
        "Lauch-Salat: Lauch, Tomaten, Zwiebel, Zitrone, Öl."
    ],
    "Rettich": [
        "Rettich-Salat: Rettich, Zwiebel, Essig, Öl, Dill.",
        "Rettich-Suppe: Rettich, Zwiebel, Kartoffeln, Gemüsebrühe.",
        "Rettich-Pfannkuchen: Rettich, Mehl, Ei, Milch, Salz, Pfeffer."
    ],
    "Radieschen": [
        "Radieschen-Salat: Radieschen, Zwiebel, Essig, Öl, Dill.",
        "Radieschen-Suppe: Radieschen, Zwiebel, Kartoffeln, Gemüsebrühe.",
        "Radieschen-Pfannkuchen: Radieschen, Mehl, Ei, Milch, Salz, Pfeffer."
    ],
    "Basilikum": [
        "Basilikum-Sauce: Basilikum, Knoblauch, Nüsse, Öl, Parmesan.",
        "Basilikum-Pasta: Basilikum, Pasta, Knoblauch, Öl, Parmesan.",
        "Basilikum-Salat: Basilikum, Tomaten, Zwiebel, Zitrone, Öl."
    ],
    "Dill": [
        "Dill-Sauce: Dill, Joghurt, Zwiebel, Essig, Öl.",
        "Dill-Pasta: Dill, Pasta, Knoblauch, Öl, Parmesan.",
        "Dill-Salat: Dill, Tomaten, Gurke, Zwiebel, Zitrone, Öl."
    ],
    "Schnittlauch": [
        "Schnittlauch-Sauce: Schnittlauch, Joghurt, Zwiebel, Essig, Öl.",
        "Schnittlauch-Pasta: Schnittlauch, Pasta, Knoblauch, Öl, Parmesan.",
        "Schnittlauch-Salat: Schnittlauch, Tomaten, Gurke, Zwiebel, Zitrone, Öl."
    ],
    "Thymian": [
        "Thymian-Braten: Hähnchen, Thymian, Zitrone, Öl, Salz, Pfeffer.",
        "Thymian-Suppe: Thymian, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Thymian-Pasta: Thymian, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Oregano": [
        "Oregano-Pizza: Oregano, Tomaten, Mozzarella, Olivenöl.",
        "Oregano-Suppe: Oregano, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Oregano-Pasta: Oregano, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Rosmarin": [
        "Rosmarin-Braten: Hähnchen, Rosmarin, Zitrone, Öl, Salz, Pfeffer.",
        "Rosmarin-Suppe: Rosmarin, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Rosmarin-Pasta: Rosmarin, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Schnittknoblauch": [
        "Schnittknoblauch-Sauce: Schnittknoblauch, Joghurt, Zwiebel, Essig, Öl.",
        "Schnittknoblauch-Pasta: Schnittknoblauch, Pasta, Knoblauch, Öl, Parmesan.",
        "Schnittknoblauch-Salat: Schnittknoblauch, Tomaten, Gurke, Zwiebel, Zitrone, Öl."
    ],
    "Zitronengras": [
        "Zitronengras-Curry: Zitronengras, Hähnchen, Kokosmilch, Zwiebel, Knoblauch.",
        "Zitronengras-Suppe: Zitronengras, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Zitronengras-Pasta: Zitronengras, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Chili": [
        "Chili-Sauce: Chili, Tomaten, Zwiebel, Knoblauch, Essig, Öl.",
        "Chili-Curry: Chili, Hähnchen, Kokosmilch, Zwiebel, Knoblauch.",
        "Chili-Salat: Chili, Tomaten, Gurke, Zwiebel, Zitrone, Öl."
    ],
    "Paprikapulver": [
        "Paprikapulver-Pasta: Paprikapulver, Pasta, Knoblauch, Öl, Parmesan.",
        "Paprikapulver-Suppe: Paprikapulver, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Paprikapulver-Braten: Hähnchen, Paprikapulver, Zitrone, Öl, Salz, Pfeffer."
    ],
    "Kurkumapulver": [
        "Kurkumapulver-Tee: Kurkumapulver, Wasser, Honig, Zitrone.",
        "Kurkumapulver-Curry: Kurkumapulver, Hähnchen, Kokosmilch, Zwiebel, Knoblauch.",
        "Kurkumapulver-Smoothie: Kurkumapulver, Joghurt, Milch, Honig."
    ],
    "Sesam": [
        "Sesam-Salat: Sesam, Salat, Tomaten, Gurke, Zwiebel, Zitrone, Öl.",
        "Sesam-Pasta: Sesam, Pasta, Knoblauch, Öl, Parmesan.",
        "Sesam-Brot: Sesam, Mehl, Ei, Zucker, Butter."
    ],
    "Tahini": [
        "Tahini-Dressing: Tahini, Zitrone, Wasser, Salz, Pfeffer.",
        "Tahini-Pasta: Tahini, Pasta, Knoblauch, Öl, Parmesan.",
        "Tahini-Salat: Tahini, Salat, Tomaten, Gurke, Zwiebel, Zitrone."
    ],
    "Mandelmus": [
        "Mandelmus-Smoothie: Mandelmus, Joghurt, Milch, Honig.",
        "Mandelmus-Kuchen: Mandelmus, Mehl, Ei, Zucker, Butter.",
        "Mandelmus-Sauce: Mandelmus, Joghurt, Zwiebel, Essig, Öl."
    ],
    "Haselnussmus": [
        "Haselnussmus-Smoothie: Haselnussmus, Joghurt, Milch, Honig.",
        "Haselnussmus-Kuchen: Haselnussmus, Mehl, Ei, Zucker, Butter.",
        "Haselnussmus-Sauce: Haselnussmus, Joghurt, Zwiebel, Essig, Öl."
    ],
    "Kokosnussmus": [
        "Kokosnussmus-Smoothie: Kokosnussmus, Joghurt, Milch, Honig.",
        "Kokosnussmus-Kuchen: Kokosnussmus, Mehl, Ei, Zucker, Butter.",
        "Kokosnussmus-Sauce: Kokosnussmus, Joghurt, Zwiebel, Essig, Öl."
    ],
    "Peanutbutter": [
        "Peanutbutter-Smoothie: Peanutbutter, Joghurt, Milch, Honig.",
        "Peanutbutter-Kuchen: Peanutbutter, Mehl, Ei, Zucker, Butter.",
        "Peanutbutter-Sauce: Peanutbutter, Joghurt, Zwiebel, Essig, Öl."
    ],
    "Nussmus": [
        "Nussmus-Smoothie: Nussmus, Joghurt, Milch, Honig.",
        "Nussmus-Kuchen: Nussmus, Mehl, Ei, Zucker, Butter.",
        "Nussmus-Sauce: Nussmus, Joghurt, Zwiebel, Essig, Öl."
    ],
    "Kokosraspeln": [
        "Kokosraspeln-Salat: Kokosraspeln, Salat, Tomaten, Gurke, Zwiebel, Zitrone, Öl.",
        "Kokosraspeln-Pasta: Kokosraspeln, Pasta, Knoblauch, Öl, Parmesan.",
        "Kokosraspeln-Kuchen: Kokosraspeln, Mehl, Ei, Zucker, Butter."
    ],
    "Ahornsirup": [
        "Ahornsirup-Smoothie: Ahornsirup, Joghurt, Milch, Honig.",
        "Ahornsirup-Kuchen: Ahornsirup, Mehl, Ei, Zucker, Butter.",
        "Ahornsirup-Dressing: Ahornsirup, Essig, Öl, Senf, Salz."
    ],
    "Balsamico": [
        "Balsamico-Dressing: Balsamico, Öl, Senf, Honig, Salz.",
        "Balsamico-Suppe: Balsamico, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Balsamico-Pasta: Balsamico, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Weißwein": [
        "Weißwein-Sauce: Weißwein, Sahne, Butter, Zwiebel, Knoblauch.",
        "Weißwein-Suppe: Weißwein, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Weißwein-Pasta: Weißwein, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Rotwein": [
        "Rotwein-Sauce: Rotwein, Sahne, Butter, Zwiebel, Knoblauch.",
        "Rotwein-Suppe: Rotwein, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Rotwein-Pasta: Rotwein, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Sekt": [
        "Sekt-Smoothie: Sekt, Joghurt, Milch, Honig.",
        "Sekt-Sauce: Sekt, Sahne, Butter, Zwiebel, Knoblauch.",
        "Sekt-Suppe: Sekt, Kartoffeln, Zwiebel, Gemüsebrühe."
    ],
    "Bier": [
        "Bier-Sauce: Bier, Sahne, Butter, Zwiebel, Knoblauch.",
        "Bier-Suppe: Bier, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Bier-Pasta: Bier, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Wodka": [
        "Wodka-Sauce: Wodka, Sahne, Butter, Zwiebel, Knoblauch.",
        "Wodka-Suppe: Wodka, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Wodka-Pasta: Wodka, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Whisky": [
        "Whisky-Sauce: Whisky, Sahne, Butter, Zwiebel, Knoblauch.",
        "Whisky-Suppe: Whisky, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Whisky-Pasta: Whisky, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Rum": [
        "Rum-Sauce: Rum, Sahne, Butter, Zwiebel, Knoblauch.",
        "Rum-Suppe: Rum, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Rum-Pasta: Rum, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Gin": [
        "Gin-Sauce: Gin, Sahne, Butter, Zwiebel, Knoblauch.",
        "Gin-Suppe: Gin, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Gin-Pasta: Gin, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Tequila": [
        "Tequila-Sauce: Tequila, Sahne, Butter, Zwiebel, Knoblauch.",
        "Tequila-Suppe: Tequila, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Tequila-Pasta: Tequila, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Cognac": [
        "Cognac-Sauce: Cognac, Sahne, Butter, Zwiebel, Knoblauch.",
        "Cognac-Suppe: Cognac, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Cognac-Pasta: Cognac, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Schnaps": [
        "Schnaps-Sauce: Schnaps, Sahne, Butter, Zwiebel, Knoblauch.",
        "Schnaps-Suppe: Schnaps, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Schnaps-Pasta: Schnaps, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Likör": [
        "Likör-Sauce: Likör, Sahne, Butter, Zwiebel, Knoblauch.",
        "Likör-Suppe: Likör, Kartoffeln, Zwiebel, Gemüsebrühe.",
        "Likör-Pasta: Likör, Pasta, Knoblauch, Öl, Parmesan."
    ],
    "Sardinen": [
        "Sardinen-Salat: Sardinen, Tomaten, Zwiebel, Zitrone, Öl.",
        "Sardinen-Pasta: Sardinen, Pasta, Knoblauch, Öl, Parmesan.",
        "Sardinen-Braten: Sardinen, Zwiebel, Knoblauch, Öl, Salz, Pfeffer."
    ],
    "Hering": [
        "Hering-Salat: Hering, Kartoffeln, Zwiebel, Gurke, Essig, Öl.",
        "Hering-Pasta: Hering, Pasta, Knoblauch, Öl, Parmesan.",
        "Hering-Braten: Hering, Zwiebel, Knoblauch, Öl, Salz, Pfeffer."
    ],
    "Sardellen": [
        "Sardellen-Salat: Sardellen, Tomaten, Zwiebel, Zitrone, Öl.",
        "Sardellen-Pasta: Sardellen, Pasta, Knoblauch, Öl, Parmesan.",
        "Sardellen-Braten: Sardellen, Zwiebel, Knoblauch, Öl, Salz, Pfeffer."
    ],
    "Sardellenpaste": [
        "Sardellenpaste-Sauce: Sardellenpaste, Joghurt, Zwiebel, Essig, Öl.",
        "Sardellenpaste-Pasta: Sardellenpaste, Pasta, Knoblauch, Öl, Parmesan.",
        "Sardellenpaste-Salat: Sardellenpaste, Salat, Tomaten, Gurke, Zwiebel, Zitrone, Öl."
    ],
    "Sardellenöl": [
        "Sardellenöl-Sauce: Sardellenöl, Joghurt, Zwiebel, Essig, Öl.",
        "Sardellenöl-Pasta: Sardellenöl, Pasta, Knoblauch, Öl, Parmesan.",
        "Sardellenöl-Salat: Sardellenöl, Salat, Tomaten, Gurke, Zwiebel, Zitrone, Öl."
    ],
    "Sardellensoße": [
        "Sardellensoße-Sauce: Sardellensoße, Joghurt, Zwiebel, Essig, Öl.",
        "Sardellensoße-Pasta: Sardellensoße, Pasta, Knoblauch, Öl, Parmesan.",
        "Sardellensoße-Salat: Sardellensoße, Salat, Tomaten, Gurke, Zwiebel, Zitrone, Öl."
    ],
    "Sardellenfilet": [
        "Sardellenfilet-Salat: Sardellenfilet, Tomaten, Zwiebel, Zitrone, Öl.",
        "Sardellenfilet-Pasta: Sardellenfilet, Pasta, Knoblauch, Öl, Parmesan.",
        "Sardellenfilet-Braten: Sardellenfilet, Zwiebel, Knoblauch, Öl, Salz, Pfeffer."
    ],
}

# ================================
# 📥 Funktionen
# ================================

def load_data():
    try:
        with open("smartfridge_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("smartfridge_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ================================
# 🖥️ App-Start
# ================================

# ✅ Sicherstellen, dass APP_NAME und ICON vor st.set_page_config() definiert sind
st.set_page_config(page_title=APP_NAME, layout="wide", page_icon=ICON)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff3cd, #fff9e6);
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3 {
        color: #2C3E50;
        text-align: center;
    }
    .stButton>button {
        background-color: #FFA500;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 8px rgba(255, 165, 0, 0.3);
    }
    .stButton>button:hover {
        background-color: #FF8C00;
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #FFA500;
        padding: 10px;
    }
    .stWarning {
        background-color: #fff3cd;
        border-left: 5px solid #FFA500;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
    }
    .stInfo {
        background-color: #fff9e6;
        border-left: 5px solid #FFD700;
        padding: 10px;
        border-radius: 8px;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

st.title(f"{ICON} {APP_NAME}")
st.markdown("### 🍽️ Lebensmittel im Blick.")

# --- Daten laden ---
if "lebensmittel" not in st.session_state:
    st.session_state.lebensmittel = load_data()

# --- Eingabeformular ---
with st.container():
    st.markdown("### 📥 Lebensmittel hinzufügen")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", placeholder="z. B. Milch", key="name_input")
    with col2:
        date_input = st.date_input("Ablaufdatum", value=datetime.date.today(), key="date_input")
        date_str = date_input.strftime("%d.%m.%Y")

    if st.button("✅ Hinzufügen", key="add_btn"):
        if not name:
            st.warning("Bitte gib einen Namen ein.")
        else:
            try:
                days = DEFAULT_HALTBARKEIT.get(name, 7)
                expected_date = datetime.datetime.strptime(date_str, "%d.%m.%Y") + datetime.timedelta(days=days)
                st.session_state.lebensmittel.append({
                    "name": name,
                    "date": date_str,
                    "expected": expected_date.strftime("%d.%m.%Y"),
                    "days_left": days
                })
                save_data(st.session_state.lebensmittel)
                st.success(f"✅ {name} hinzugefügt! Ablauf: {date_str}")
            except Exception as e:
                st.error(f"❌ Fehler: {e}")

# --- Liste der Lebensmittel mit Löschen-Button ---
st.markdown("### 🛒 Dein NomNom")
now = datetime.datetime.now()

if st.session_state.lebensmittel:
    for i, item in enumerate(st.session_state.lebensmittel):
        name = item["name"]
        date_str = item["date"]
        expected_date = datetime.datetime.strptime(item["expected"], "%d.%m.%Y")
        days_left = (expected_date - now).days

        # Farbe basierend auf Tagen
        if days_left <= 0:
            color = "red"
            icon = "💀"
        elif days_left <= 3:
            color = "orange"
            icon = "⚠️"
        elif days_left <= 7:
            color = "yellow"
            icon = "🟡"
        else:
            color = "green"
            icon = "🟢"

        # Container mit Löschen-Button
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"""
                <div style='padding: 12px; margin: 8px 0; border-radius: 12px; background: white; box-shadow: 0 2px 6px rgba(0,0,0,0.1); border-left: 5px solid {color};'>
                    <strong style='color: {color}; font-size: 16px;'>{icon} {name}</strong>
                    <br>
                    <small style='color: #666;'>Ablauf: {date_str} ({days_left} Tage)</small>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                if st.button("🗑️", key=f"del_{i}"):
                    st.session_state.lebensmittel.pop(i)
                    save_data(st.session_state.lebensmittel)
                    st.rerun()

        # Rezeptvorschläge: Nur bei kurz vor Ablauf alle anzeigen
        if name in REZEPTE:
            if days_left <= 3:
                st.warning(f"🔥 **Schnell verbrauchen!** Rezepte für **{name}**:")
                for recipe in REZEPTE[name]:
                    st.markdown(f"• {recipe}")
            else:
                recipe = REZEPTE[name][0]
                st.info(f"💡 Rezept: {recipe}")

            # Hinzufügen-Button
            if st.button(f"➕ Hinzufügen: {name}", key=f"add_from_recipe_{i}"):
                if any(item["name"] == name for item in st.session_state.lebensmittel):
                    st.warning(f"⚠️ {name} ist bereits in der Liste.")
                else:
                    st.session_state.lebensmittel.append({
                        "name": name,
                        "date": now.strftime("%d.%m.%Y"),
                        "expected": (now + datetime.timedelta(days=DEFAULT_HALTBARKEIT.get(name, 7))).strftime("%d.%m.%Y"),
                        "days_left": DEFAULT_HALTBARKEIT.get(name, 7)
                    })
                    save_data(st.session_state.lebensmittel)
                    st.success(f"✅ {name} hinzugefügt (aus Rezept)")
else:
    st.info("📭 Noch keine Lebensmittel hinzugefügt.")

# --- Warnung vor Ablauf ---
now = datetime.datetime.now()
expiring = [item["name"] for item in st.session_state.lebensmittel if (datetime.datetime.strptime(item["date"], "%d.%m.%Y") - now).days <= 3 and (datetime.datetime.strptime(item["date"], "%d.%m.%Y") - now).days >= 0]
if expiring:
    st.warning(f"⚠️ Achtung: Folgende Lebensmittel laufen bald ab: {', '.join(expiring)}")

# --- Footer ---
st.markdown("---")

st.markdown("💡 *NomNom – Dein persönlicher Küchenhelfer für weniger Verschwendung.*")

