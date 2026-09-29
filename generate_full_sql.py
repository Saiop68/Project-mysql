import datetime
import sqlite3
import re
import os

# Complete SQL Dataset Generator, Verifier, and Output Writer

REF_DATE_STR = "2026-10-01"
REF_DATE = datetime.date(2026, 10, 1)

# --- 1. PRODUCT CATEGORIES (300 products) ---
stationery = [
    ("Reynolds 045 Fine Carbure Ball Pen Blue", 10, None),
    ("Reynolds 045 Fine Carbure Ball Pen Black", 10, None),
    ("Cello Butterflow Classic Blue Ball Pen", 15, None),
    ("Cello Butterflow Classic Black Ball Pen", 15, None),
    ("Parker Vector Standard Chrome Trim Roller Ball Pen", 299, None),
    ("Pilot V5 Liquid Ink Roller Ball Pen Blue", 60, None),
    ("Pilot V7 Hi-Tecpoint Roller Ball Pen Black", 70, None),
    ("Camlin Kokuyo Whiteboard Marker Black", 30, None),
    ("Camlin Kokuyo Whiteboard Marker Blue", 30, None),
    ("Camlin Permanent Marker Pen Black", 25, None),
    ("Luxor Highliter Neon Yellow Pack of 1", 25, None),
    ("Luxor Highliter Neon Green Pack of 1", 25, None),
    ("Classmate Pulse Single Line Spiral Notebook 200 Pages", 85, None),
    ("Classmate Long Notebook 160 Pages Ruled", 65, None),
    ("Classmate Long Notebook 240 Pages Ruled", 95, None),
    ("Navneet Youva Soft Bound Long Book 180 Pages", 70, None),
    ("JK Easy Copier A4 Paper 75 GSM 500 Sheets", 340, None),
    ("B2C A4 Executive Bond Paper 85 GSM 100 Sheets", 180, None),
    ("Apsara Platinum Eraser", 5, None),
    ("Nataraj 621 HB Wood Pencils Pack of 10", 50, None),
    ("Apsara Matt 2B Dark Pencils Pack of 10", 60, None),
    ("Camlin Exam Mechanical Pencil 0.7mm", 40, None),
    ("Camlin Lead Tubes 0.7mm 2B", 15, None),
    ("Kangaro No 10 Stapler", 65, None),
    ("Kangaro 10-1M Staple Pins Pack", 15, None),
    ("Kangaro Heavy Duty Stapler HP-45", 350, None),
    ("Kangaro 24/6 Staple Pins Pack", 30, None),
    ("Fevicol MR General Purpose Squeezy Glue 50g", 25, None),
    ("Fevikwik Instant Adhesive 1g", 5, None),
    ("Faber-Castell Vinyl Eraser Pack of 2", 20, None)
]

school_supplies = [
    ("Camlin Scholar Mathematical Drawing Geometry Box", 120, None),
    ("Camlin Artist Acrylic Colour 12 Shades", 260, None),
    ("Faber-Castell Triangular Colour Pencils 12 Shades", 75, None),
    ("Doms Oil Pastels 25 Shades", 90, None),
    ("Doms Plastic Crayons 16 Shades", 60, None),
    ("Camlin Student Water Colour Cake 24 Shades", 110, None),
    ("Classmate Drawing Book Unruled 40 Pages", 45, None),
    ("Youva Craft Paper Assorted Origami Sheets 50 Pack", 55, None),
    ("Faber-Castell Modelling Clay Dough 6 Colours", 80, None),
    ("Milton Kool Steel Kid Stainless Steel Water Bottle 500ml", 399, None),
    ("Milton Electron Electric Lunch Box 3 Container", 899, None),
    ("Cello Puro Sports Water Bottle 750ml", 110, None),
    ("Classmate Asteroid Mathematical Drawing Box", 175, None),
    ("Cello Maxriter Ball Pen Pack of 5", 50, None),
    ("Maped Universal Geometry Compass", 85, None),
    ("Navneet School Atlas India and World", 180, None),
    ("Pidilite Rangeela Tempera Colours 12 Shades", 70, None),
    ("Scotch Child Safe Scissors 5 Inch", 65, None),
    ("Casio FX-82MS 2nd Gen Scientific Calculator", 575, None),
    ("Casio MJ-120D Plus Desktop Basic Calculator", 425, None),
    ("Doms Water Colour Tubes 12 Shades", 130, None),
    ("Doms Groove Slim Pencils Pack of 10", 70, None),
    ("Classmate Pulse 6 Subject Spiral Notebook 300 Pages", 190, None),
    ("Youva Practical Geometry Book Hardbound 120 Pages", 95, None),
    ("Nataraj Sharpener and Eraser Combo Pack", 20, None)
]

office_supplies = [
    ("Kangaro Perforator Two Hole Punch DP-52", 140, None),
    ("Solo Display Book 20 Pockets A4 Size", 130, None),
    ("Solo Ring Binder File 2 Ring A4 Size", 160, None),
    ("Solo Clear Expanding File Folder 12 Pockets", 275, None),
    ("Post-it Sticky Notes 3x3 Inch Yellow 100 Sheets", 55, None),
    ("3M Scotch Magic Tape Transparent 19mm x 30m", 95, None),
    ("Wonder Tape Heavy Duty Packaging Brown Tape 2 Inch x 50m", 65, None),
    ("Solo Desk Organizer 4 Compartments Smoke Grey", 240, None),
    ("Deli Metal Wire Mesh Pen Holder Stand", 99, None),
    ("Oddy Multipurpose Label Stickers A4 24 Labels Sheet 100 Pack", 380, None),
    ("Kangaro Metal Paper Binder Clips 19mm Box of 12", 45, None),
    ("Kangaro Metal Paper Binder Clips 32mm Box of 12", 85, None),
    ("Solo Separator Index File Dividers 1 to 10", 50, None),
    ("Cello Tape Dispenser Medium Core", 110, None),
    ("Solo Executive Document Bag Waterproof", 320, None),
    ("Kores White Correction Fluid Pen 7ml", 35, None),
    ("Deli Heavy Duty Paper Cutter 18mm Utility Knife", 65, None),
    ("Solo Presentation Folder Clear View Pack of 5", 125, None),
    ("Kangaro Pinless Paper Stapler", 190, None),
    ("3M Command Medium Utility Hooks 2 Pack", 210, None),
    ("Solo Card Holder Business Card Album 120 Cards", 145, None),
    ("Deli Desktop Tape Dispenser Heavy Base", 185, None),
    ("Solo Report Cover Files Pack of 10", 110, None),
    ("Oddy White Board Duster Magnetic", 55, None),
    ("Solo Visitor Identity Badge Holder with Lanyard Pack of 5", 95, None)
]

electronics_accessories = [
    ("Portronics Konnect CL Type-C to Lightning Cable 1.2m", 299, None),
    ("Portronics 65W GaN Multi-Port Fast Charger", 1499, None),
    ("Boat Rugged v3 Micro USB Fast Charging Cable 1.5m", 199, None),
    ("Boat Deuce 300 2-in-1 Type-C and Micro USB Cable", 299, None),
    ("Mi 2A Fast Charger Adapter with Micro USB Cable", 499, None),
    ("Duracell Chota Power AAA Alkaline Batteries Pack of 4", 140, None),
    ("Duracell Ultra Alkaline AA Batteries Pack of 4", 180, None),
    ("Eveready Carbon Zinc D Size 1.5V Batteries Pack of 2", 70, None),
    ("Logitech M90 Wired USB Optical Mouse", 299, None),
    ("Logitech B170 Wireless Optical Mouse", 599, None),
    ("Zebronics Zeb-Comfort Wired USB Mouse", 149, None),
    ("Zebronics Zeb-Dash Wireless Optical Mouse", 349, None),
    ("Portronics Clamp X Car Mobile Holder", 399, None),
    ("Lapcare Screen Cleaning Gel Kit 100ml with Microfiber Cloth", 149, None),
    ("Amazon Basics High Speed HDMI Cable 1.8m 4K Support", 280, None),
    ("Portronics Prime 3.5mm Aux Audio Male to Male Cable 1m", 120, None),
    ("Gizga Essentials Laptop Stand Ergonomic Aluminium", 699, None),
    ("Portronics MODESK Universal Mobile Table Stand", 160, None),
    ("TP-Link Nano USB Wi-Fi Adapter TL-WN725N 150Mbps", 499, None),
    ("Zebronics Zeb-Pluto 2.0 Multimedia USB Speakers", 399, None),
    ("GM 3 Pin Multi Plug Adapter with Indicator", 90, None),
    ("GM Modular 4 Socket Spike Guard Surge Protector 2m", 440, None),
    ("SanDisk Cruzer Blade 32GB USB 2.0 Flash Drive", 349, None),
    ("SanDisk Ultra 64GB MicroSDXC Memory Card Class 10", 489, None),
    ("Ambrane 10000mAh Power Bank Lithium Polymer", 899, None)
]

household_items = [
    ("Gala NoDust Floor Broom Plastic Handle", 180, None),
    ("Gala Quick Spin Mop with Microfiber Refill", 999, None),
    ("Gala Twin Dustpan and Brush Set", 140, None),
    ("Scotch-Brite Scrub Sponge Pack of 3", 80, None),
    ("Scotch-Brite Stainless Steel Heavy Scrubber Pack of 2", 60, None),
    ("Scotch-Brite High Performance Microfiber Kitchen Wiper", 110, None),
    ("Scotch-Brite Bathroom Squeegee Floor Wiper", 220, None),
    ("Milton Spotzero Floor Cleaning Wiper Medium", 190, None),
    ("Cello Checkers Plastic Airtight Storage Jar 1000ml Pack of 4", 299, None),
    ("Cello Aqua Cool Plastic Water Bottle 1000ml Pack of 4", 220, None),
    ("Borosil Vision Glass Tumbler Set 295ml Pack of 6", 380, None),
    ("Pigeon Polypropylene Cutting Chopping Board Large", 199, None),
    ("Cello Gripper Plastic Clothes Clips Pegs Pack of 24", 85, None),
    ("Nayasa Plastic Multi Storage Utility Basket Medium", 130, None),
    ("Milton Plastic Insulated Hot Pot Casserole 1500ml", 450, None),
    ("All Out Ultra Mosquito Vaporizer Machine with Refill", 125, None),
    ("Good knight Gold Flash Liquid Mosquito Repellent Refill 45ml", 85, None),
    ("Odonil Room Air Freshener Blocks 50g Pack of 4", 190, None),
    ("Godrej aer pocket Bathroom Fragrance Gel 10g", 60, None),
    ("Mangaldeep Temple Agarbatti Sandalwood Incense Sticks 120g", 75, None),
    ("Cycle Pure Agarbatti Yagna Incense Cones Pack of 30", 65, None),
    ("Camphor Pure Kapur Tablets for Pooja 100g", 120, None),
    ("Pigeon Stainless Steel Vegetable Peeler and Knife Set", 110, None),
    ("Wonderchef Multi Utility Stainless Steel Kitchen Scissors", 175, None),
    ("Milton Stainless Steel Insulated Tea Flask 1000ml", 699, None),
    ("Kuber Industries Door Mat Anti Skid Coir 40x60 cm", 220, None),
    ("Sparkle Aluminum Kitchen Foil 18m Roll", 145, None),
    ("Oddy Food Parchment Baking Paper Roll 20m", 170, None),
    ("Scotch-Brite Heavy Duty Kitchen Gloves Pair Medium", 130, None),
    ("Tupperware Dry Storage Container 600ml", 260, None)
]

groceries = [
    # Expired (12)
    ("Aashirvaad Superior MP Sharbati Whole Wheat Atta 1kg", 68, "2026-03-15"),
    ("Fortune Sunlite Refined Sunflower Oil 1L Pouch", 145, "2026-04-20"),
    ("Tata Sampann Unpolished Toor Dal 1kg", 185, "2026-05-10"),
    ("Madhur Pure and Hygienic Sugar 1kg", 52, "2026-02-18"),
    ("Fortune Premium Kachi Ghani Pure Mustard Oil 1L", 160, "2026-06-25"),
    ("Everest Tikhalal Hot and Red Chilli Powder 200g", 84, "2026-07-12"),
    ("Catch Coriander Powder Dhaniya 200g", 61, "2026-01-20"),
    ("Catch Turmeric Powder Haldi 200g", 58, "2026-08-14"),
    ("MDH Chana Masala Spice Blend 100g", 82, "2026-09-05"),
    ("Tata Salt Lite Low Sodium Iodized Salt 1kg", 45, "2026-08-30"),
    ("Saffola Gold Pro Healthy Lifestyle Edible Oil 1L", 175, "2026-07-28"),
    ("Fortune Soya Chunks High Protein 200g", 50, "2026-06-15"),
    
    # Expiring soon (7)
    ("Amul Pure Ghee 500ml Tin", 330, "2026-10-08"),
    ("Aashirvaad Select 100 Percent Sharbati Wheat Flour 5kg", 320, "2026-10-15"),
    ("Tata Sampann Unpolished Moong Dal Yellow 1kg", 170, "2026-10-22"),
    ("Mother Dairy Pure Cow Ghee 1L Pouch", 590, "2026-10-12"),
    ("Fortune Biryani Special Basmati Rice 1kg", 140, "2026-10-25"),
    ("Catch Super Garam Masala Powder 100g", 92, "2026-10-18"),
    ("Patanjali Pure Mustard Oil 1L", 155, "2026-10-27"),

    # Future (26)
    ("Daawat Rozana Gold Basmati Rice 5kg", 499, "2027-04-15"),
    ("India Gate Basmati Rice Feast Rozzana 1kg", 115, "2027-02-28"),
    ("Tata Salt Vacuum Evaporated Iodized Salt 1kg", 28, "2027-08-10"),
    ("Tata Sampann Unpolished Chana Dal 1kg", 125, "2027-03-20"),
    ("Tata Sampann Unpolished Urad Dal Whole 1kg", 195, "2027-05-15"),
    ("Aashirvaad Superior MP Whole Wheat Atta 5kg", 265, "2027-01-30"),
    ("Pillsbury Chakki Fresh Whole Wheat Atta 10kg", 480, "2027-03-10"),
    ("Fortune Sunlite Refined Sunflower Oil 5L Jar", 699, "2027-06-25"),
    ("Gemini Pure Refined Sunflower Oil 1L", 142, "2027-02-15"),
    ("Dhara Kachi Ghani Mustard Oil 1L Poly Pack", 158, "2027-04-10"),
    ("Saffola Total Pro Heart Conscious Edible Oil 5L", 949, "2027-07-20"),
    ("Everest Garam Masala Powder 100g Box", 90, "2027-09-15"),
    ("Everest Kitchen King Masala 100g", 85, "2027-10-12"),
    ("MDH Deggi Mirch Mild Red Chilli Powder 100g", 95, "2027-11-20"),
    ("MDH Chunky Chat Masala 100g", 78, "2027-08-25"),
    ("Badshah Pav Bhaji Masala 100g", 74, "2027-05-30"),
    ("Catch Black Pepper Powder Kali Mirch 100g", 120, "2027-06-18"),
    ("Tata Sampann Pure Kashmiri Red Chilli Powder 100g", 98, "2027-07-14"),
    ("24 Mantra Organic Raw Peanuts 500g", 135, "2027-03-25"),
    ("24 Mantra Organic Besan Gram Flour 500g", 85, "2027-04-18"),
    ("Rajdhani Poha Thick Pressed Flakes 500g", 48, "2027-01-20"),
    ("MTR Roasted Rava Sooji Semolina 500g", 55, "2027-03-15"),
    ("Quaker Rolled Oats 1kg Pouch", 199, "2027-06-10"),
    ("Kellogg's Corn Flakes Original 875g Family Pack", 360, "2027-08-22"),
    ("Amul Pasteurised Salted Butter 500g Block", 275, "2027-02-10"),
    ("Nestle Everyday Dairy Whitener Milk Powder 400g", 240, "2027-09-18")
]

snacks = [
    # Expired (12)
    ("Lay's India's Magic Masala Potato Chips 50g", 20, "2026-05-12"),
    ("Kurkure Masala Munch Crispy Corn Puffs 85g", 20, "2026-06-18"),
    ("Haldiram's Nagpur Aloo Bhujia 150g", 48, "2026-07-04"),
    ("Parle-G Gold Glucose Biscuits 1kg Value Pack", 120, "2026-08-10"),
    ("Britannia Good Day Cashew Cookies 200g", 45, "2026-04-25"),
    ("Sunfeast Dark Fantasy Choco Fills 300g", 125, "2026-08-28"),
    ("Bingo Mad Angles Achaari Masti Crisps 66g", 20, "2026-03-22"),
    ("Haldiram's Classic Salted Peanuts 200g", 55, "2026-07-15"),
    ("Bikaji Bhujia Sev Bikaneri 400g", 130, "2026-06-30"),
    ("Cadbury Dairy Milk Silk Chocolate Bar 150g", 175, "2026-08-05"),
    ("Nestle KitKat 4 Finger Chocolate Wafer 38.5g", 30, "2026-09-02"),
    ("Britannia Marie Gold Crisp Tea Biscuits 250g", 38, "2026-05-20"),

    # Expiring soon (7)
    ("Maggi 2-Minute Masala Instant Noodles 70g Single Pack", 14, "2026-10-06"),
    ("Maggi 2-Minute Masala Instant Noodles 280g Pack of 4", 56, "2026-10-14"),
    ("Britannia Treat Jim Jam Cream Biscuits 150g", 35, "2026-10-20"),
    ("Haldiram's Moong Dal Crispy Salted Snack 200g", 58, "2026-10-10"),
    ("Lay's Spanish Tomato Tango Potato Chips 50g", 20, "2026-10-26"),
    ("Cadbury Celebrations Chocolate Gift Box 130g", 150, "2026-10-18"),
    ("Kissan Fresh Tomato Ketchup Bottle 950g", 145, "2026-10-24"),

    # Future (16)
    ("Parle-G Original Glucose Biscuits 250g", 25, "2027-02-15"),
    ("Britannia Bourbon Chocolate Cream Biscuits 150g", 35, "2027-01-20"),
    ("Sunfeast Mom's Magic Cashew and Almond Biscuits 200g", 45, "2027-03-12"),
    ("Britannia NutriChoice Digestive Fibre Biscuits 250g", 55, "2027-04-18"),
    ("Haldiram's Khatta Meetha Savory Snack Mixture 400g", 110, "2027-05-25"),
    ("Haldiram's Panchrattan Spicy Mixture 200g", 95, "2027-03-30"),
    ("Bikaji All in One Kuch-Kuch Spicy Mixture 400g", 125, "2027-06-15"),
    ("Act II Golden Sizzlin Butter Popcorn 150g", 40, "2027-02-28"),
    ("Doritos Nacho Cheese Flavoured Tortilla Chips 60g", 30, "2027-01-10"),
    ("Pringles Original Potato Crisps Canister 107g", 115, "2027-07-20"),
    ("Pringles Sour Cream and Onion Potato Crisps 107g", 115, "2027-08-15"),
    ("Cadbury Dairy Milk Chocolate Bar 50g", 45, "2027-04-05"),
    ("Nestle Munch Crunchy Wafer Bar 25g Pack of 4", 40, "2027-03-08"),
    ("Ching's Secret Schezwan Instant Hakka Noodles 240g", 60, "2027-05-12"),
    ("Maggi Special Masala Spicy Noodles Pack of 4", 72, "2027-06-28"),
    ("Yippee Mood Masala Instant Noodles 260g Pack of 4", 55, "2027-04-22")
]

beverages = [
    # Expired (6)
    ("Tropicana 100 Percent Orange Fruit Juice 1L Tetra", 130, "2026-04-12"),
    ("Real Fruit Power Mixed Fruit Juice 1L Tetra", 125, "2026-06-08"),
    ("Paper Boat Mango Aamras Drink 200ml", 35, "2026-07-19"),
    ("Raw Pressery Valencia Orange Cold Pressed Juice 250ml", 99, "2026-08-22"),
    ("Red Bull Energy Drink Can 250ml", 125, "2026-05-30"),
    ("Coca-Cola Original Taste Sparkling Soft Drink 750ml", 40, "2026-09-08"),

    # Expiring soon (4)
    ("Real Fruit Power Alphonso Mango Fruit Juice 1L", 130, "2026-10-09"),
    ("Tropicana Delight Apple Fruit Juice 1L Tetra", 120, "2026-10-16"),
    ("Frooti Real Mango Drink 1.2L Bottle", 70, "2026-10-22"),
    ("Amul Kool Badam Flavoured Milk Can 200ml", 35, "2026-10-15"),

    # Future (15)
    ("Brooke Bond Red Label Strong CTC Tea 1kg", 490, "2027-08-14"),
    ("Brooke Bond Red Label Strong CTC Tea 500g", 260, "2027-07-20"),
    ("Brooke Bond Taj Mahal Rich CTC Tea Leaves 500g", 360, "2027-09-10"),
    ("Tata Tea Gold Rich Taste & Irresistible Aroma 500g", 290, "2027-06-15"),
    ("Tata Tea Premium Desh Ki Chai Leaf Tea 1kg", 440, "2027-10-05"),
    ("Wagh Bakri Premium CTC Blend Tea Leaves 500g", 270, "2027-05-18"),
    ("Tetley Pure Green Tea Bags Box of 100 Tea Bags", 450, "2027-11-20"),
    ("Lipton Pure & Light Mint Green Tea Bags Box of 25", 160, "2027-04-25"),
    ("Nescafe Classic Pure 100 Percent Instant Coffee Glass Jar 100g", 325, "2027-12-15"),
    ("Nescafe Classic Pure Instant Coffee Pouch 50g", 165, "2027-08-30"),
    ("Bru Instant Coffee and Chicory Blend Jar 100g", 240, "2027-07-12"),
    ("Bru Gold 100 Percent Pure Granulated Coffee 100g", 310, "2027-09-25"),
    ("Cadbury Bournvita Chocolate Nutrition Drink Jar 1kg", 415, "2027-06-30"),
    ("Horlicks Classic Malt Health Drink Jar 1kg", 430, "2027-05-10"),
    ("Hershey's Chocolate Syrup Flavoured Bottle 623g", 220, "2027-04-15")
]

personal_care = [
    # Expired (5)
    ("Dettol Original Germ Protection Bathing Soap 75g", 36, "2026-03-25"),
    ("Dove Cream Beauty Bathing Bar Soap 100g Pack of 3", 185, "2026-05-14"),
    ("Lifebuoy Total 10 Germ Protection Soap 125g Pack of 4", 140, "2026-06-20"),
    ("Colgate Strong Teeth Anticavity Toothpaste 150g", 98, "2026-07-10"),
    ("Pepsodent Expert Protection Germi Check Toothpaste 140g", 95, "2026-08-16"),

    # Expiring soon (4)
    ("Medimix Ayurvedic 18 Herbs Classic Bathing Soap 125g", 48, "2026-10-08"),
    ("Santoor Sandal and Turmeric Bathing Soap 125g Pack of 4", 160, "2026-10-18"),
    ("Head and Shoulders Anti Dandruff Cool Menthol Shampoo 180ml", 190, "2026-10-25"),
    ("Patanjali Dant Kanti Ayurvedic Natural Toothpaste 200g", 110, "2026-10-12"),

    # Future (26)
    ("Pears Pure and Gentle Glycerine Bathing Bar 125g Pack of 3", 240, "2027-09-15"),
    ("Fiama Di Wills Gel Bathing Bar Blackcurrant 125g Pack of 3", 225, "2027-08-20"),
    ("Mysore Sandal Pure Sandalwood Oil Bath Soap 150g", 95, "2027-11-10"),
    ("Clinic Plus Strong & Long Health Shampoo 340ml", 220, "2027-07-15"),
    ("Clinic Plus Strong & Long Health Shampoo 650ml", 399, "2027-12-05"),
    ("Sunsilk Co-Creations Stunning Black Shine Shampoo 370ml", 265, "2027-06-20"),
    ("Dove Intense Repair Shampoo with Keratin Actives 340ml", 320, "2027-10-22"),
    ("Tresemme Keratin Smooth Hair Shampoo with Argan Oil 340ml", 360, "2027-09-18"),
    ("Pantene Advanced Hair Fall Control Shampoo 340ml", 295, "2027-08-12"),
    ("L'Oreal Paris Total Repair 5 Restoring Shampoo 340ml", 345, "2027-11-25"),
    ("Parachute 100 Percent Pure Coconut Hair Oil 500ml Bottle", 199, "2027-10-10"),
    ("Bajaj Almond Drops Non Sticky Hair Oil with Vitamin E 300ml", 215, "2027-08-28"),
    ("Dabur Amla Hair Oil for Long & Strong Hair 450ml", 195, "2027-07-30"),
    ("Dabur Red Ayurvedic Toothpaste 300g Combo Pack", 165, "2027-06-14"),
    ("Sensodyne Fresh Mint Sensitive Teeth Toothpaste 150g", 230, "2027-09-20"),
    ("Oral-B Cross Action Deep Clean Soft Toothbrush Pack of 4", 175, "2028-03-15"),
    ("Colgate ZigZag Charcoal Antibacterial Toothbrush Pack of 6", 160, "2028-02-20"),
    ("Gillette Mach3 Men Shaving Razor with 1 Cartridge", 299, "2028-05-10"),
    ("Gillette Classic Sensitive Men Shaving Foam 418g", 245, "2027-12-18"),
    ("Dettol Original Instant Antiseptic Disinfectant Liquid 550ml", 215, "2027-09-05"),
    ("Nivea Men Fresh Active Deodorant Spray 150ml", 199, "2027-08-15"),
    ("Fogg Men Fragrance Body Spray Marco 120ml", 230, "2027-10-14"),
    ("Vaseline Intensive Care Deep Moisture Body Lotion 400ml", 310, "2027-11-30"),
    ("Nivea Soft Light Moisturizing Cream 200ml", 280, "2027-07-22"),
    ("Himalaya Purifying Neem Face Wash Gentle Cleanser 150ml", 185, "2027-08-08"),
    ("Garnier Men Acno Fight Anti Pimple Face Wash 100g", 170, "2027-05-25")
]

cleaning = [
    # Expired (5)
    ("Lizol Disinfectant Surface Floor Cleaner Citrus 500ml", 110, "2026-04-10"),
    ("Harpic Power Plus Original Disinfectant Toilet Cleaner 500ml", 99, "2026-06-15"),
    ("Vim Dishwash Liquid Gel Lemon 250ml Bottle", 58, "2026-07-20"),
    ("Surf Excel Quick Wash Detergent Powder 500g", 85, "2026-08-12"),
    ("Rin Advanced Detergent Bar Soap 250g Pack of 4", 75, "2026-05-30"),

    # Expiring soon (3)
    ("Colin Glass and Household Cleaner Spray 500ml", 105, "2026-10-07"),
    ("Ariel Matic Top Load Washing Powder 1kg", 240, "2026-10-19"),
    ("Godrej aer Matic Automatic Room Freshener Spray 225ml", 550, "2026-10-25"),

    # Future (17)
    ("Surf Excel Easy Wash Detergent Powder 1kg Pouch", 145, "2027-07-10"),
    ("Surf Excel Matic Front Load Liquid Detergent 1L Pouch", 235, "2027-09-15"),
    ("Surf Excel Matic Top Load Detergent Powder 2kg Box", 460, "2027-10-20"),
    ("Ariel Complete Detergent Washing Powder 1kg", 155, "2027-06-18"),
    ("Tide Plus Extra Power Detergent Powder Lemon 2kg", 260, "2027-08-14"),
    ("Wheel 2 in 1 Detergent Powder Green 1kg", 72, "2027-05-22"),
    ("Vim Dishwash Liquid Gel Lemon Fragrance 750ml Refill", 155, "2027-11-10"),
    ("Pril Kraft Dishwash Liquid Green Lime Active Gel 750ml", 160, "2027-09-28"),
    ("Vim Dishwash Anti Smell Lemon Bar Soap 300g Pack of 3", 65, "2027-04-30"),
    ("Lizol Disinfectant Surface Floor Cleaner Floral 2L", 380, "2027-12-15"),
    ("Harpic Power Plus Disinfectant Toilet Cleaner 1L", 185, "2027-08-25"),
    ("Domex Disinfectant Bleach Toilet and Surface Cleaner 1L", 175, "2027-07-12"),
    ("Comfort After Wash Fabric Conditioner Lily Fresh 860ml", 225, "2027-10-05"),
    ("Dettol Multi Surface Disinfectant Spray Spring Blossom 500ml", 199, "2027-09-18"),
    ("Kiwi Kleen Bathroom and Tile Spray Cleaner 500ml", 145, "2027-06-10"),
    ("Hit Anti Mosquito and Roach Flying Insect Killer Spray 625ml", 320, "2027-11-20"),
    ("Hit Cockroach Specialist Crawling Insect Killer Spray 400ml", 240, "2027-08-04")
]

product_categories_list = [
    ("Stationery", stationery),
    ("School Supplies", school_supplies),
    ("Office Supplies", office_supplies),
    ("Electronics Accessories", electronics_accessories),
    ("Household Items", household_items),
    ("Groceries", groceries),
    ("Snacks", snacks),
    ("Beverages", beverages),
    ("Personal Care", personal_care),
    ("Cleaning Products", cleaning)
]

all_products = []
for cat_name, items in product_categories_list:
    for name, price, exp in items:
        all_products.append({
            "name": name,
            "price": price,
            "expiry": exp,
            "category": cat_name
        })

# --- 2. CUSTOMERS DATA (500 customers) ---
import test_customers
all_customers = test_customers.customers

# --- 3. SQL STRING FORMATTER ---
def sql_escape_str(val):
    if val is None:
        return "NULL"
    return "'" + val.replace("'", "''") + "'"

def sql_date(val):
    if val is None:
        return "NULL"
    return f"'{val}'"

# --- 4. GENERATE SQL STATEMENTS ---
sql_lines = []

sql_lines.append("-- ============================================================================")
sql_lines.append("-- MySQL Retail Shop Management Dataset")
sql_lines.append("-- Target Schema: MySQL 8.0+")
sql_lines.append("-- Compatible with MySQL Workbench, phpMyAdmin, and Command Line Client")
sql_lines.append("-- ============================================================================\n")
sql_lines.append("CREATE DATABASE IF NOT EXISTS shop_management;")
sql_lines.append("USE shop_management;\n")

sql_lines.append("-- Drop existing tables if re-running")
sql_lines.append("DROP TABLE IF EXISTS shop;")
sql_lines.append("DROP TABLE IF EXISTS customers;\n")

sql_lines.append("-- ----------------------------------------------------------------------------")
sql_lines.append("-- Table structure for table `customers`")
sql_lines.append("-- ----------------------------------------------------------------------------")
sql_lines.append("CREATE TABLE customers (")
sql_lines.append("    customer_id INT PRIMARY KEY AUTO_INCREMENT,")
sql_lines.append("    customer_name VARCHAR(100) NOT NULL,")
sql_lines.append("    address VARCHAR(150),")
sql_lines.append("    city VARCHAR(100),")
sql_lines.append("    postal_code INT")
sql_lines.append(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;\n")

sql_lines.append("-- ----------------------------------------------------------------------------")
sql_lines.append("-- Table structure for table `shop`")
sql_lines.append("-- ----------------------------------------------------------------------------")
sql_lines.append("CREATE TABLE shop (")
sql_lines.append("    product_id INT PRIMARY KEY AUTO_INCREMENT,")
sql_lines.append("    product_price INT NOT NULL,")
sql_lines.append("    product_name VARCHAR(100) NOT NULL,")
sql_lines.append("    product_expiry DATE")
sql_lines.append(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;\n")

sql_lines.append("-- ============================================================================")
sql_lines.append("-- Data Insertion: customers (500 records)")
sql_lines.append("-- Multi-row INSERT statements (50 rows per batch)")
sql_lines.append("-- ============================================================================\n")

CUST_BATCH_SIZE = 50
for b_start in range(0, len(all_customers), CUST_BATCH_SIZE):
    batch = all_customers[b_start:b_start + CUST_BATCH_SIZE]
    batch_num = b_start // CUST_BATCH_SIZE + 1
    total_batches = (len(all_customers) + CUST_BATCH_SIZE - 1) // CUST_BATCH_SIZE
    sql_lines.append(f"-- Customers Batch {batch_num} of {total_batches} (Rows {b_start + 1} to {b_start + len(batch)})")
    sql_lines.append("INSERT INTO customers (customer_name, address, city, postal_code) VALUES")
    
    value_rows = []
    for c_name, c_addr, c_city, c_pin in batch:
        escaped_name = sql_escape_str(c_name)
        escaped_addr = sql_escape_str(c_addr)
        escaped_city = sql_escape_str(c_city)
        value_rows.append(f"({escaped_name}, {escaped_addr}, {escaped_city}, {c_pin})")
    
    sql_lines.append(",\n".join(value_rows) + ";\n")

sql_lines.append("-- ============================================================================")
sql_lines.append("-- Data Insertion: shop (300 records)")
sql_lines.append("-- Multi-row INSERT statements (50 rows per batch)")
sql_lines.append("-- ============================================================================\n")

PROD_BATCH_SIZE = 50
for b_start in range(0, len(all_products), PROD_BATCH_SIZE):
    batch = all_products[b_start:b_start + PROD_BATCH_SIZE]
    batch_num = b_start // PROD_BATCH_SIZE + 1
    total_batches = (len(all_products) + PROD_BATCH_SIZE - 1) // PROD_BATCH_SIZE
    sql_lines.append(f"-- Shop Products Batch {batch_num} of {total_batches} (Rows {b_start + 1} to {b_start + len(batch)})")
    sql_lines.append("INSERT INTO shop (product_price, product_name, product_expiry) VALUES")
    
    value_rows = []
    for p in batch:
        p_name_esc = sql_escape_str(p["name"])
        p_exp_str = sql_date(p["expiry"])
        value_rows.append(f"({p['price']}, {p_name_esc}, {p_exp_str})")
        
    sql_lines.append(",\n".join(value_rows) + ";\n")

full_sql_content = "\n".join(sql_lines)

# Write to file
with open("shop_management.sql", "w", encoding="utf-8") as f:
    f.write(full_sql_content)

print(f"Generated shop_management.sql ({len(full_sql_content)} bytes)")

# --- 5. TEST AGAINST SQLITE FOR SYNTAX AND ANALYTICAL ACCURACY ---
con = sqlite3.connect(":memory:")
cur = con.cursor()

# We need to adapt MySQL CREATE TABLE syntax to SQLite memory test:
# Remove DATABASE / USE / ENGINE / DEFAULT CHARSET
sqlite_sql = re.sub(r"CREATE DATABASE .*?;", "", full_sql_content, flags=re.DOTALL)
sqlite_sql = re.sub(r"USE .*?;", "", sqlite_sql)
sqlite_sql = re.sub(r"INT PRIMARY KEY AUTO_INCREMENT", "INTEGER PRIMARY KEY AUTOINCREMENT", sqlite_sql)
sqlite_sql = re.sub(r"\) ENGINE=InnoDB.*?;", ");", sqlite_sql)

cur.executescript(sqlite_sql)
con.commit()

# Run Analytical Queries
cur.execute("SELECT COUNT(*) FROM customers;")
total_cust_db = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM shop;")
total_prod_db = cur.fetchone()[0]

cur.execute("SELECT COUNT(DISTINCT city) FROM customers;")
total_cities_db = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM shop WHERE product_expiry IS NOT NULL;")
prod_with_exp_db = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM shop WHERE product_expiry IS NULL;")
prod_without_exp_db = cur.fetchone()[0]

cur.execute(f"SELECT COUNT(*) FROM shop WHERE product_expiry < '{REF_DATE_STR}';")
expired_db = cur.fetchone()[0]

cur.execute(f"SELECT COUNT(*) FROM shop WHERE product_expiry >= '{REF_DATE_STR}' AND product_expiry <= '2026-10-31';")
expiring_soon_db = cur.fetchone()[0]

cur.execute("SELECT MIN(product_price), MAX(product_price), AVG(product_price) FROM shop;")
min_p, max_p, avg_p = cur.fetchone()

# Additional analytical queries from prompt:
cur.execute("SELECT COUNT(*) FROM customers WHERE city = 'Mumbai';")
mumbai_count = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM customers WHERE customer_name LIKE 'A%';")
a_name_count = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM (SELECT city, COUNT(*) as c FROM customers GROUP BY city HAVING COUNT(*) > 20);")
having_20_count = cur.fetchone()[0]

print("\n--- Analytical Query Verification ---")
print(f"Total Customers: {total_cust_db}")
print(f"Total Products: {total_prod_db}")
print(f"Total Cities: {total_cities_db}")
print(f"Product Categories: {len(product_categories_list)}")
print(f"Products with expiry dates: {prod_with_exp_db}")
print(f"Products without expiry dates: {prod_without_exp_db}")
print(f"Expired products: {expired_db}")
print(f"Products expiring within 30 days: {expiring_soon_db}")
print(f"Minimum product price: ₹{min_p}")
print(f"Maximum product price: ₹{max_p}")
print(f"Average product price: ₹{avg_p:.2f}")
print(f"Customers in Mumbai: {mumbai_count}")
print(f"Customers with name LIKE 'A%': {a_name_count}")
print(f"Cities with COUNT(*) > 20: {having_20_count}")
