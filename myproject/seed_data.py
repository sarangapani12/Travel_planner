import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Country, City, Category, Place, PlaceImage

# Clear everything
PlaceImage.objects.all().delete()
Place.objects.all().delete()
City.objects.all().delete()
Category.objects.all().delete()
Country.objects.all().delete()

print("🗑  Cleared existing data...")

# Country
india = Country.objects.create(name="India", code="IN", flag_emoji="🇮🇳")

# Categories
temple   = Category.objects.create(name="Temple",   icon="🛕")
nature   = Category.objects.create(name="Nature",   icon="🌿")
heritage = Category.objects.create(name="Heritage", icon="🏛")
beach    = Category.objects.create(name="Beach",    icon="🏖")
palace   = Category.objects.create(name="Palace",   icon="👑")
adventure= Category.objects.create(name="Adventure",icon="🏔")
wildlife = Category.objects.create(name="Wildlife", icon="🐘")

print("✅ Categories created...")

# ── CITIES ──────────────────────────────────────────────────────────────────

mumbai = City.objects.create(
    country=india, name="Mumbai", slug="mumbai",
    description="The city of dreams — a vibrant coastal metropolis bursting with culture, history, and Bollywood magic.",
    cover_image="https://images.unsplash.com/photo-1567157577867-05ccb1388e66?w=800",
    latitude=19.0760, longitude=72.8777, budget_level="medium"
)
jaipur = City.objects.create(
    country=india, name="Jaipur", slug="jaipur",
    description="The Pink City — a royal desert gem filled with majestic forts, ornate palaces, and vivid bazaars.",
    cover_image="https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800",
    latitude=26.9124, longitude=75.7873, budget_level="budget"
)
kerala = City.objects.create(
    country=india, name="Kerala", slug="kerala",
    description="God's Own Country — serene backwaters, lush tea hills, spice gardens, and golden beaches.",
    cover_image="https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800",
    latitude=10.8505, longitude=76.2711, budget_level="medium"
)
varanasi = City.objects.create(
    country=india, name="Varanasi", slug="varanasi",
    description="The spiritual soul of India — ancient ghats, sacred rituals, and the eternal flow of the Ganges.",
    cover_image="https://images.unsplash.com/photo-1540962351504-03099e0a754b?w=800",
    latitude=25.3176, longitude=82.9739, budget_level="budget"
)
manali = City.objects.create(
    country=india, name="Manali", slug="manali",
    description="The adventure capital of the Himalayas — snow-capped peaks, pine forests, and thrilling mountain passes.",
    cover_image="https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800",
    latitude=32.2432, longitude=77.1892, budget_level="medium"
)
arunachal = City.objects.create(
    country=india, name="Arunachal Pradesh", slug="arunachal-pradesh",
    description="The Land of the Dawn-Lit Mountains — pristine monasteries, tribal culture, and untouched Himalayan wilderness.",
    cover_image="https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=800",
    latitude=27.0844, longitude=93.6053, budget_level="budget"
)
assam = City.objects.create(
    country=india, name="Assam", slug="assam",
    description="The gateway to Northeast India — famous for one-horned rhinos, rolling tea estates, and the mighty Brahmaputra.",
    cover_image="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
    latitude=26.2006, longitude=92.9376, budget_level="budget"
)
manipur = City.objects.create(
    country=india, name="Manipur", slug="manipur",
    description="The Jewel of India — a land of floating lakes, classical dance, and breathtaking valley landscapes.",
    cover_image="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    latitude=24.6637, longitude=93.9063, budget_level="budget"
)
meghalaya = City.objects.create(
    country=india, name="Meghalaya", slug="meghalaya",
    description="The Abode of Clouds — living root bridges, the world's wettest village, and crystal-clear river canyons.",
    cover_image="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800",
    latitude=25.4670, longitude=91.3662, budget_level="budget"
)
mizoram = City.objects.create(
    country=india, name="Mizoram", slug="mizoram",
    description="The Land of the Blue Mountains — rolling hills, vibrant Mizo culture, and some of India's cleanest cities.",
    cover_image="https://images.unsplash.com/photo-1586348943529-beaae6c28db9?w=800",
    latitude=23.1645, longitude=92.9376, budget_level="budget"
)
nagaland = City.objects.create(
    country=india, name="Nagaland", slug="nagaland",
    description="The Land of Festivals — warrior tribes, the famous Hornbill Festival, and dramatic misty mountain ranges.",
    cover_image="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800",
    latitude=26.1584, longitude=94.5624, budget_level="budget"
)
tripura = City.objects.create(
    country=india, name="Tripura", slug="tripura",
    description="India's hidden northeast gem — royal palaces, ancient temples, and lush bamboo forests.",
    cover_image="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=800",
    latitude=23.9408, longitude=91.9882, budget_level="budget"
)

print("✅ Cities created...")

# ── MUMBAI PLACES ────────────────────────────────────────────────────────────

p = Place.objects.create(
    city=mumbai, category=heritage, name="Gateway of India", slug="gateway-of-india",
    short_description="Iconic colonial arch overlooking the Arabian Sea.",
    full_description="Built in 1924 to commemorate the visit of King George V, the Gateway of India stands as Mumbai's most iconic landmark. This 26-metre basalt arch blends Hindu and Muslim architectural styles and faces the majestic Arabian Sea. It was also the spot from which the last British troops departed India in 1948, marking the symbolic end of colonial rule. Today it's a bustling promenade with street food, boat rides to Elephanta Caves, and the grand Taj Mahal Palace Hotel as its backdrop.",
    cover_image="https://images.unsplash.com/photo-1529253355930-ddbe423a2ac7?w=800",
    best_time_to_visit="October to February", entry_fee="Free", rating=4.7,
    tips="Visit early morning before crowds arrive. Take a boat ride to Elephanta Caves from here — well worth the trip!"
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1529253355930-ddbe423a2ac7?w=600", caption="Gateway at dusk")
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1567157577867-05ccb1388e66?w=600", caption="Aerial view of Mumbai harbour")

p = Place.objects.create(
    city=mumbai, category=beach, name="Marine Drive", slug="marine-drive",
    short_description="Mumbai's famous 3.6km seafront promenade — the Queen's Necklace.",
    full_description="Marine Drive is a C-shaped boulevard stretching 3.6 kilometres along the coast of South Mumbai. Named the Queen's Necklace for the way its streetlights glitter at night like a string of pearls, it is one of India's most photographed landmarks. The wide sidewalk is perfect for an evening stroll as the sun dips into the Arabian Sea.",
    cover_image="https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800",
    best_time_to_visit="November to March", entry_fee="Free", rating=4.6,
    tips="Come at sunset for the best views. Monsoon season (June–August) is dramatic and beautiful too!"
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=600", caption="Marine Drive at night")

p = Place.objects.create(
    city=mumbai, category=heritage, name="Elephanta Caves", slug="elephanta-caves",
    short_description="UNESCO World Heritage rock-cut temples on a tranquil island.",
    full_description="The Elephanta Caves are a collection of cave temples carved into solid rock on Elephanta Island, about 10 kilometres from the Mumbai harbour. A UNESCO World Heritage Site, the caves are dedicated primarily to the Hindu god Shiva and date back to between the 5th and 8th centuries. The most famous sculpture is the Trimurti — a three-headed bust of Shiva standing nearly six metres tall.",
    cover_image="https://images.unsplash.com/photo-1594735366979-6257b6d42575?w=800",
    best_time_to_visit="October to March", entry_fee="₹40 Indians / ₹600 foreigners", rating=4.5,
    tips="Take the ferry from Gateway of India. Wear comfortable shoes — there's a toy train but walking is more fun!"
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1594735366979-6257b6d42575?w=600", caption="The Trimurti sculpture")

# ── JAIPUR PLACES ────────────────────────────────────────────────────────────

p = Place.objects.create(
    city=jaipur, category=palace, name="Amber Fort", slug="amber-fort",
    short_description="Magnificent hilltop fort palace overlooking Maota Lake.",
    full_description="Amber Fort, also known as Amer Fort, is a stunning example of Rajput architecture perched on a rugged hillside just 11 kilometres from Jaipur. Built in 1592 by Raja Man Singh I, the fort complex is a sprawling blend of Hindu and Mughal architectural styles. The Sheesh Mahal (Palace of Mirrors) inside is breathtaking — thousands of tiny mirrors embedded in the ceiling create a galaxy-like effect when a single candle is lit.",
    cover_image="https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800",
    best_time_to_visit="October to March", entry_fee="₹100 Indians / ₹500 foreigners", rating=4.8,
    tips="Book a sound and light show ticket in the evening — absolutely magical. Arrive by 8am to avoid crowds."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1477587458883-47145ed94245?w=600", caption="Amber Fort from Maota Lake")

p = Place.objects.create(
    city=jaipur, category=palace, name="City Palace", slug="city-palace-jaipur",
    short_description="Royal palace complex in the heart of the Pink City.",
    full_description="The City Palace of Jaipur is a majestic complex of courtyards, gardens, and buildings that was the seat of the Maharaja of Jaipur. Built between 1729 and 1732 by Maharaja Sawai Jai Singh II, the palace blends Rajasthani, Mughal, and European architectural styles. The royal family still resides in part of the palace.",
    cover_image="https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800",
    best_time_to_visit="October to February", entry_fee="₹200 Indians / ₹700 foreigners", rating=4.7,
    tips="The combined ticket covers multiple attractions. Visit the rooftop for panoramic views of the Pink City."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1599661046289-e31897846e41?w=600", caption="City Palace courtyard")

p = Place.objects.create(
    city=jaipur, category=heritage, name="Hawa Mahal", slug="hawa-mahal",
    short_description="The Palace of Winds — iconic five-storey honeycombed façade.",
    full_description="The Hawa Mahal, or Palace of Winds, is perhaps Jaipur's most photographed monument. Built in 1799 by Maharaja Sawai Pratap Singh, this extraordinary five-storey structure has 953 small windows called Jharokhas, decorated with intricate latticework. The palace was designed so royal ladies could observe street festivals without being seen.",
    cover_image="https://images.unsplash.com/photo-1512632578888-169bbbc64f33?w=800",
    best_time_to_visit="October to March", entry_fee="₹50 Indians / ₹200 foreigners", rating=4.6,
    tips="The best view is from outside — from the tea stall across the road. Morning light is perfect for photos."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1512632578888-169bbbc64f33?w=600", caption="Hawa Mahal facade")

# ── KERALA PLACES ────────────────────────────────────────────────────────────

p = Place.objects.create(
    city=kerala, category=nature, name="Alleppey Backwaters", slug="alleppey-backwaters",
    short_description="Tranquil network of canals, lagoons and lakes — Kerala's crown jewel.",
    full_description="The Alleppey Backwaters are a vast network of interconnected canals, rivers, lakes and inlets formed by more than 900 kilometres of waterways in Kerala. A houseboat cruise through these calm waters is one of India's most unique travel experiences — drifting past emerald paddy fields, swaying coconut palms, quaint fishing villages, and ancient temples.",
    cover_image="https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800",
    best_time_to_visit="September to March", entry_fee="Houseboat from ₹8,000/night", rating=4.9,
    tips="Book an overnight houseboat for the full experience. Choose a premium boat for better food and comfort."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=600", caption="Houseboat on the backwaters")

p = Place.objects.create(
    city=kerala, category=nature, name="Munnar Tea Gardens", slug="munnar-tea-gardens",
    short_description="Rolling emerald hills blanketed in lush tea plantations.",
    full_description="Munnar is a breathtaking hill station in the Western Ghats of Kerala, sitting at an altitude of 1,600 metres. Once the summer resort of the British South India government, it is now famous for its vast stretches of tea plantations that carpet the rolling hills in every shade of green imaginable.",
    cover_image="https://images.unsplash.com/photo-1545579133-99bb5ad189be?w=800",
    best_time_to_visit="September to May", entry_fee="Free (Tea Museum ₹75)", rating=4.8,
    tips="Stay in a tea estate bungalow for an immersive experience. The drive from Cochin is incredibly scenic."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1545579133-99bb5ad189be?w=600", caption="Tea estates at dawn")

p = Place.objects.create(
    city=kerala, category=beach, name="Varkala Beach", slug="varkala-beach",
    short_description="Dramatic cliffside beach with mineral springs and sea views.",
    full_description="Varkala is unlike any other beach in India. A stunning red laterite cliff drops dramatically down to a pristine stretch of golden sand and the deep blue Arabian Sea. The clifftop is lined with cafes, yoga studios, and Ayurveda centres offering spectacular sea views.",
    cover_image="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
    best_time_to_visit="October to March", entry_fee="Free", rating=4.7,
    tips="Walk north along the cliff path at sunset. The southern end of the beach near the temple is less crowded."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600", caption="Varkala cliffs at sunset")

# ── VARANASI PLACES ──────────────────────────────────────────────────────────

p = Place.objects.create(
    city=varanasi, category=temple, name="Kashi Vishwanath Temple", slug="kashi-vishwanath",
    short_description="One of the holiest Hindu temples, dedicated to Lord Shiva.",
    full_description="The Kashi Vishwanath Temple is one of the most famous Hindu temples in the world and is dedicated to Lord Shiva. Located in the narrow lanes of Varanasi on the western bank of the Ganges, it is one of the twelve Jyotirlingas — the holiest of Shiva temples. The new Kashi Vishwanath Corridor, inaugurated in 2021, has transformed the approach to the temple.",
    cover_image="https://images.unsplash.com/photo-1640516630234-96f8c3608e7b?w=800",
    best_time_to_visit="October to March", entry_fee="Free", rating=4.8,
    tips="Visit during the Mangala Aarti at 3am or Shringar Aarti at sunset for the most spiritual experience."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1640516630234-96f8c3608e7b?w=600", caption="Temple spires at golden hour")

p = Place.objects.create(
    city=varanasi, category=heritage, name="Dashashwamedh Ghat", slug="dashashwamedh-ghat",
    short_description="The main ghat of Varanasi — home to the spectacular Ganga Aarti.",
    full_description="Dashashwamedh Ghat is the main and most spectacular ghat in Varanasi. Every evening at sunset, the famous Ganga Aarti takes place here — a mesmerising ritual where priests perform a fire ceremony with large flaming torches, incense, flowers, and chanting to the Ganges river. The ghat comes alive with hundreds of devotees and the hypnotic sound of bells and mantras.",
    cover_image="https://images.unsplash.com/photo-1561361058-c24e015e4873?w=800",
    best_time_to_visit="October to February", entry_fee="Free", rating=4.9,
    tips="Take a boat on the Ganges to watch the Aarti from the water — the best view. Book early evening slots."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1561361058-c24e015e4873?w=600", caption="Ganga Aarti ceremony")

p = Place.objects.create(
    city=varanasi, category=heritage, name="Sarnath", slug="sarnath",
    short_description="Where Buddha gave his first sermon — a serene Buddhist pilgrimage site.",
    full_description="Sarnath, located just 10 kilometres from Varanasi, is one of the four most sacred Buddhist pilgrimage sites in the world. It was here that Gautama Buddha delivered his first sermon after attaining enlightenment, setting in motion the Wheel of Dharma. The Dhamek Stupa, rising 43 metres, marks the exact spot of that first teaching. The Archaeological Museum here houses the famous Lion Capital of Ashoka, which became India's national emblem.",
    cover_image="https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800",
    best_time_to_visit="October to March", entry_fee="₹30 Indians / ₹500 foreigners", rating=4.6,
    tips="Combine with a Varanasi Ghats visit. Early morning is peaceful and perfect for meditation."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=600", caption="Dhamek Stupa at Sarnath")

# ── MANALI PLACES ────────────────────────────────────────────────────────────

p = Place.objects.create(
    city=manali, category=adventure, name="Rohtang Pass", slug="rohtang-pass",
    short_description="A breathtaking high-altitude mountain pass at 3,978 metres.",
    full_description="Rohtang Pass is one of India's most dramatic high-altitude passes, sitting at 3,978 metres above sea level on the eastern Pir Panjal Range of the Himalayas. The name Rohtang literally means 'pile of corpses' — a testament to the treacherous conditions travellers once faced. Today it draws thousands of visitors who come to witness the spectacular views of glaciers, deep gorges, and the Lahaul and Spiti valleys stretching endlessly beyond. Snow is present almost year-round and activities like skiing, snowboarding and sledging are hugely popular.",
    cover_image="https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800",
    best_time_to_visit="May to October", entry_fee="₹550 per vehicle (permit required)", rating=4.7,
    tips="Book your permit online at least 2 days in advance. Start early — permits are limited to 1,200 vehicles per day."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=600", caption="Snow-covered Rohtang Pass")
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1587474260584-136574528ed5?w=600", caption="Mountain views from the pass")

p = Place.objects.create(
    city=manali, category=adventure, name="Solang Valley", slug="solang-valley",
    short_description="Adventure sports paradise — skiing, paragliding and zorbing.",
    full_description="Solang Valley, nicknamed the 'Snow Point', lies about 14 kilometres from Manali and is one of Himachal Pradesh's premier adventure sports destinations. In winter, the valley transforms into a ski resort with powdery slopes perfect for beginners and intermediate skiers. In summer, the snow melts to reveal a green meadow paradise where paragliding, zorbing, horse riding, and rope activities take over. The valley is flanked by towering glaciers and offers some of the most photogenic mountain panoramas in the entire Himalayan range.",
    cover_image="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    best_time_to_visit="December to February (skiing) / May to October (adventure)", entry_fee="Activity-based (₹300–₹2000)", rating=4.6,
    tips="Try paragliding in summer for unforgettable aerial views of the valley. Book activities through certified operators only."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600", caption="Paragliding over Solang Valley")

p = Place.objects.create(
    city=manali, category=temple, name="Hadimba Devi Temple", slug="hadimba-devi-temple",
    short_description="Ancient wooden pagoda temple nestled in a cedar forest.",
    full_description="The Hadimba Devi Temple is a unique and enchanting shrine nestled amid ancient cedar forests in the Dhungiri Van Vihar park in Manali. Built in 1553 by Maharaja Bahadur Singh, this four-storey wooden pagoda-style temple is dedicated to Hadimba Devi, wife of Bhima from the Mahabharata. The temple's ornately carved wooden doorway is a masterpiece of Himachali craftsmanship. The surrounding forest of towering deodar cedars creates a mystical atmosphere unlike any other temple in India.",
    cover_image="https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?w=800",
    best_time_to_visit="March to June / September to November", entry_fee="Free", rating=4.7,
    tips="Visit early morning when the forest is misty and quiet. The Dussehra festival here is spectacular in October."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?w=600", caption="Temple among the cedar trees")

p = Place.objects.create(
    city=manali, category=nature, name="Old Manali & Manu Temple", slug="old-manali",
    short_description="The charming original village of Manali with cafes and the ancient Manu Temple.",
    full_description="Old Manali is the original settlement that predates the modern tourist town, connected by a bridge over the Manalsu stream. This charming village has a completely different character — narrow lanes lined with apple orchards, traditional Himachali stone houses, quirky cafes, and a laid-back bohemian atmosphere loved by long-stay travellers. At its heart is the Manu Temple, dedicated to the sage Manu who is believed to have survived a great flood and restarted human civilisation right here. The views of the Beas River valley from the village lanes are spectacular.",
    cover_image="https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800",
    best_time_to_visit="April to June / September to November", entry_fee="Free", rating=4.5,
    tips="Have breakfast at one of the rooftop cafes overlooking the valley. The apple orchards are stunning in spring."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=600", caption="Old Manali village lanes")

# ── MEGHALAYA PLACES ─────────────────────────────────────────────────────────

p = Place.objects.create(
    city=meghalaya, category=nature, name="Living Root Bridges", slug="living-root-bridges",
    short_description="Ancient living bridges grown from rubber tree roots — a natural wonder.",
    full_description="The Living Root Bridges of Meghalaya are one of the most extraordinary natural engineering feats on earth. The Khasi and Jaintia tribes of the Cherrapunji and Mawlynnong regions have been training the roots of rubber fig trees across streams and rivers for hundreds of years, creating strong, living bridges that grow stronger with age. The most famous is the Double Decker Root Bridge near Nongriat village — a two-storey living bridge that took over 500 years to grow. The trek to reach it winds through dense subtropical jungle, crystal streams, and traditional Khasi villages.",
    cover_image="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800",
    best_time_to_visit="October to May", entry_fee="₹50 per person", rating=4.9,
    tips="The trek to Double Decker Bridge takes 3–4 hours each way. Start early and carry water and snacks."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600", caption="Double Decker Root Bridge")

p = Place.objects.create(
    city=meghalaya, category=nature, name="Dawki River", slug="dawki-river",
    short_description="The crystal-clear river where boats appear to float on air.",
    full_description="The Dawki River, also known as the Umngot River, is one of India's most surreal natural attractions. The water is so extraordinarily clear that boats appear to float in mid-air above the riverbed. Located near the Bangladesh border in the Jaintia Hills district, the river flows through a dramatic gorge with steel-blue water of impossible clarity. The annual boat race held here in February draws teams from across the region and is a spectacular display of Khasi culture and competitive spirit.",
    cover_image="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    best_time_to_visit="October to April", entry_fee="Boat hire ₹500–₹800", rating=4.8,
    tips="Visit between November and March for the clearest water. Avoid monsoon season when the river turns muddy."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600", caption="Crystal clear Dawki River")

p = Place.objects.create(
    city=meghalaya, category=nature, name="Mawsmai Cave", slug="mawsmai-cave",
    short_description="Illuminated limestone caves with spectacular stalactite formations.",
    full_description="The Mawsmai Cave in Cherrapunji is one of the most accessible and visually stunning limestone caves in Meghalaya. Stretching 150 metres through the earth, the cave is filled with dramatic stalactites and stalagmites formed over millions of years. Narrow passages open suddenly into grand cathedral-like chambers with formations in every imaginable shape. Cherrapunji itself holds the record for the highest recorded monthly rainfall on Earth, and the landscape around the caves reflects this — every surface drips with green moss, ferns, and tropical vegetation.",
    cover_image="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
    best_time_to_visit="October to May", entry_fee="₹20 per person", rating=4.5,
    tips="The cave passage is narrow in places. Carry a small torch even though it is lit. Not suitable for claustrophobics."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600", caption="Limestone formations inside Mawsmai")

# ── ASSAM PLACES ─────────────────────────────────────────────────────────────

p = Place.objects.create(
    city=assam, category=wildlife, name="Kaziranga National Park", slug="kaziranga-national-park",
    short_description="UNESCO World Heritage Site — home to two-thirds of the world's one-horned rhinos.",
    full_description="Kaziranga National Park is one of India's greatest wildlife conservation success stories. A UNESCO World Heritage Site, it is home to the world's largest population of the endangered Indian one-horned rhinoceros — over 2,600 of them roam its vast floodplain grasslands. The park also shelters the highest density of tigers of any protected area in the world, along with wild elephants, wild water buffalo, swamp deer, and hundreds of bird species. Jeep safaris at dawn through the misty grasslands with the Himalayan foothills as a backdrop are utterly unforgettable.",
    cover_image="https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800",
    best_time_to_visit="November to April", entry_fee="₹250 Indians / ₹1000 foreigners + jeep hire", rating=4.9,
    tips="Book a dawn jeep safari in the Central Range for the best rhino sightings. Elephant safaris offer a unique perspective."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=600", caption="One-horned rhino in Kaziranga")

p = Place.objects.create(
    city=assam, category=nature, name="Majuli Island", slug="majuli-island",
    short_description="The world's largest river island — a cultural heartland of Assamese heritage.",
    full_description="Majuli is the world's largest inhabited river island, sitting in the middle of the mighty Brahmaputra River in Assam. This extraordinary island is the cultural capital of Assam and the cradle of neo-Vaishnavite culture, with over 20 ancient Satras (monastery-monasteries) that have preserved Assamese dance, music, mask-making, and manuscript traditions for over 500 years. The island's flat landscape of paddy fields, fishing villages, and wetlands is home to rare migratory birds and offers a glimpse of a vanishing way of life.",
    cover_image="https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=800",
    best_time_to_visit="October to March", entry_fee="Ferry ₹20 / Free entry", rating=4.6,
    tips="Stay overnight in a local guesthouse to experience the island after day-trippers leave. Visit a Satra in the morning."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=600", caption="Sunrise over Majuli Island")

p = Place.objects.create(
    city=assam, category=nature, name="Brahmaputra River Cruise", slug="brahmaputra-river-cruise",
    short_description="Cruise one of Asia's mightiest rivers past sandbanks and river dolphins.",
    full_description="The Brahmaputra is one of Asia's great rivers — wide, powerful, and deeply sacred to the people of Assam. A cruise on the Brahmaputra is one of the most spectacular ways to experience the Northeast. Multi-day luxury cruises sail between Jorhat and Guwahati, stopping at river islands, wildlife sanctuaries, and ancient temples along the way. The river is home to the endangered Gangetic river dolphin, and sightings are common on quieter stretches. At sunset, the golden light on the river's immense breadth is a sight that stays with you forever.",
    cover_image="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    best_time_to_visit="November to March", entry_fee="Cruise from ₹15,000 per person", rating=4.7,
    tips="Book the Antara or Charaidew luxury cruises for the best experience. Binoculars are essential for dolphin spotting."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600", caption="Sunset on the Brahmaputra")

# ── ARUNACHAL PRADESH PLACES ─────────────────────────────────────────────────

p = Place.objects.create(
    city=arunachal, category=temple, name="Tawang Monastery", slug="tawang-monastery",
    short_description="India's largest monastery — a spiritual citadel in the Himalayan clouds.",
    full_description="The Tawang Monastery is the largest monastery in India and the second largest in the world after the Potala Palace in Lhasa. Perched at 3,048 metres in the remote Tawang district, it was founded in the 17th century and houses over 450 monks. The monastery complex contains a 8-metre tall gilded statue of Lord Buddha, an invaluable library of ancient scriptures and thangkas, and offers sweeping views of snow-capped Himalayan peaks. The drive to Tawang itself — crossing the legendary Se La Pass at 4,176 metres — is one of the most dramatic mountain journeys in India.",
    cover_image="https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=800",
    best_time_to_visit="March to October", entry_fee="₹50 per person", rating=4.9,
    tips="An Inner Line Permit (ILP) is required to enter Arunachal Pradesh. Apply online at least a week in advance."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1598091383021-15ddea10925d?w=600", caption="Tawang Monastery at dawn")

p = Place.objects.create(
    city=arunachal, category=nature, name="Ziro Valley", slug="ziro-valley",
    short_description="A UNESCO-nominated valley of rice fields, pine hills and Apatani culture.",
    full_description="Ziro Valley is one of Northeast India's most beautiful and culturally rich destinations. This wide, flat valley in the Lower Subansiri district is home to the Apatani tribe, known for their unique sustainable farming practices — growing rice and fish simultaneously in the same flooded fields — a technique so remarkable it has been nominated as a UNESCO World Heritage cultural landscape. Pine-forested hills surround the valley on all sides, and the traditional Apatani villages with their bamboo houses and distinctive tattoo traditions offer a fascinating window into a way of life that has remained largely unchanged for centuries.",
    cover_image="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    best_time_to_visit="September to November", entry_fee="ILP required", rating=4.8,
    tips="The Ziro Music Festival in September is one of India's best boutique music festivals — held amid rice fields."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600", caption="Rice terraces in Ziro Valley")

# ── MANIPUR PLACES ───────────────────────────────────────────────────────────

p = Place.objects.create(
    city=manipur, category=nature, name="Loktak Lake", slug="loktak-lake",
    short_description="The largest freshwater lake in Northeast India with floating islands.",
    full_description="Loktak Lake is the largest freshwater lake in Northeast India and one of the most unique ecosystems on the planet. What makes Loktak truly extraordinary are the Phumdis — floating islands of heterogeneous mass of vegetation, soil and organic matter that drift across the lake's surface. The world's only floating national park, Keibul Lamjao, exists on these Phumdis and is the last natural habitat of the endangered Sangai deer — also known as the dancing deer — found nowhere else on Earth. Sunrise over the lake when the mist hangs low over the floating islands is absolutely otherworldly.",
    cover_image="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    best_time_to_visit="October to March", entry_fee="₹10 per person", rating=4.7,
    tips="Hire a boat from Sendra Island for the best views of the floating Phumdis. Dawn is magical on the lake."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600", caption="Sunrise over Loktak Lake")

p = Place.objects.create(
    city=manipur, category=heritage, name="Kangla Fort", slug="kangla-fort",
    short_description="The ancient seat of Manipuri royalty — a sacred historical complex.",
    full_description="Kangla Fort was the ancient capital and sacred seat of the Manipuri kings for nearly two thousand years. Located in the heart of Imphal, the fort is one of the most important historical and archaeological sites in Northeast India. The complex contains ancient temples, sacred ponds, the iconic Kangla Sha dragon statues at its entrance, and the ruins of royal palaces that tell the story of Manipur's proud and independent history. The fort was occupied by British forces and later by the Indian Army, finally being returned to the people of Manipur in 2004.",
    cover_image="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=800",
    best_time_to_visit="October to March", entry_fee="₹10 Indians / ₹100 foreigners", rating=4.5,
    tips="Hire a local guide to understand the deep cultural significance of each section. The evening light is beautiful here."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=600", caption="Kangla Fort entrance")

# ── MIZORAM PLACES ───────────────────────────────────────────────────────────

p = Place.objects.create(
    city=mizoram, category=nature, name="Phawngpui Blue Mountain", slug="phawngpui-blue-mountain",
    short_description="Mizoram's highest peak — the abode of gods with spectacular panoramic views.",
    full_description="Phawngpui, or the Blue Mountain, is the highest peak in Mizoram at 2,157 metres and one of the most beautiful natural landscapes in the entire Northeast. The mountain and its surrounding national park are named for the blue-purple haze that colours the mountain ranges when viewed from a distance. The summit offers breathtaking 360-degree panoramas of rolling mountain ranges stretching to Myanmar. The park is rich in biodiversity — rare orchids, carnivorous plants, Himalayan serow, and the clouded leopard all inhabit its forests.",
    cover_image="https://images.unsplash.com/photo-1586348943529-beaae6c28db9?w=800",
    best_time_to_visit="October to April", entry_fee="₹50 per person", rating=4.6,
    tips="The trek to the summit takes 2–3 hours. Carry warm layers — temperatures drop sharply at the top."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1586348943529-beaae6c28db9?w=600", caption="View from Phawngpui summit")

p = Place.objects.create(
    city=mizoram, category=nature, name="Vantawng Falls", slug="vantawng-falls",
    short_description="Mizoram's tallest waterfall cascading through dense jungle.",
    full_description="Vantawng Falls is the tallest waterfall in Mizoram and one of the highest in Northeast India, plunging over 229 metres through dense tropical forest in the Serchhip district. The falls are named after a legendary Mizo chief and hold deep cultural significance for the local community. The journey to the falls winds through spectacular mountain scenery and traditional Mizo villages, and the viewing platform offers a dramatic frontal view of the entire cascade. The surrounding forest is pristine and teeming with birdlife.",
    cover_image="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800",
    best_time_to_visit="September to November (post-monsoon)", entry_fee="Free", rating=4.5,
    tips="Best visited after the monsoon when the falls are at full flow. The road can be challenging — use a 4WD vehicle."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600", caption="Vantawng Falls in full flow")

# ── NAGALAND PLACES ──────────────────────────────────────────────────────────

p = Place.objects.create(
    city=nagaland, category=heritage, name="Hornbill Festival", slug="hornbill-festival",
    short_description="India's greatest tribal festival — 10 days of culture, dance and tradition.",
    full_description="The Hornbill Festival is Nagaland's most celebrated event and one of the greatest cultural festivals in all of India. Held every year from December 1st to 10th at the Kisama Heritage Village near Kohima, the festival brings together all 16 major Naga tribes to showcase their rich cultural heritage — traditional dances, war cries, indigenous games, crafts, and music performances. Named after the Great Indian Hornbill — a bird of immense cultural significance to the Naga people — the festival transforms Kisama into a kaleidoscope of colour, sound, and ceremony that is utterly unlike anything else in India.",
    cover_image="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800",
    best_time_to_visit="December 1–10 only", entry_fee="₹200 per day", rating=5.0,
    tips="Book accommodation in Kohima months in advance. The opening ceremony on December 1st is the most spectacular day."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600", caption="Naga warriors at Hornbill Festival")

p = Place.objects.create(
    city=nagaland, category=heritage, name="Kohima War Cemetery", slug="kohima-war-cemetery",
    short_description="A moving WWII memorial at the site of one of history's most decisive battles.",
    full_description="The Kohima War Cemetery is one of the most beautifully maintained and emotionally moving war memorials in Asia. Located on the former tennis court of the Deputy Commissioner's bungalow — the very ground where one of World War II's most critical battles was fought in 1944 — the cemetery honours the 1,421 soldiers of the Allied Forces who died stopping the Japanese advance into India. The Battle of Kohima has been called the Stalingrad of the East, and the famous Kohima Epitaph inscribed here — 'When you go home, tell them of us and say, For your tomorrow, we gave our today' — moves every visitor who reads it.",
    cover_image="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=800",
    best_time_to_visit="October to May", entry_fee="Free", rating=4.8,
    tips="Visit in the early morning for quiet reflection. The memorial is immaculately maintained by the Commonwealth War Graves Commission."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=600", caption="Kohima War Cemetery")

# ── TRIPURA PLACES ───────────────────────────────────────────────────────────

p = Place.objects.create(
    city=tripura, category=palace, name="Ujjayanta Palace", slug="ujjayanta-palace",
    short_description="A magnificent royal palace now housing Tripura's state museum.",
    full_description="Ujjayanta Palace is the most iconic landmark in Tripura and one of the finest examples of colonial-era Indo-Saracenic architecture in Northeast India. Built between 1899 and 1901 by Maharaja Radha Kishore Manikya, the palace sits at the heart of Agartala surrounded by Mughal-style gardens and two artificial lakes. The white marble palace features ornate Mughal domes, carved teak wood interiors, and a magnificent throne room. The palace was converted into the Tripura State Museum in 2011 and now houses a remarkable collection of tribal artefacts, royal costumes, and natural history exhibits.",
    cover_image="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=800",
    best_time_to_visit="October to March", entry_fee="₹20 Indians / ₹200 foreigners", rating=4.6,
    tips="The illuminated palace at night is stunning — walk around the garden after sunset. The museum closes on Mondays."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=600", caption="Ujjayanta Palace at dusk")

p = Place.objects.create(
    city=tripura, category=temple, name="Neermahal Water Palace", slug="neermahal-water-palace",
    short_description="India's largest water palace — a stunning Mughal-Hindu palace in a lake.",
    full_description="Neermahal is India's largest water palace and one of the most unique architectural wonders of Northeast India. Built in 1938 by Maharaja Bir Bikram Kishore Manikya in the middle of the Rudrasagar Lake, this stunning palace blends Mughal and Hindu architectural styles seamlessly. The white and red palace rises directly from the waters of the lake, surrounded by lotus flowers and visited by migratory birds. The only way to reach the palace is by boat, and the journey across the lake — particularly at sunset when the palace glows golden against the sky — is pure magic.",
    cover_image="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800",
    best_time_to_visit="October to March", entry_fee="₹20 + ₹80 boat fare", rating=4.7,
    tips="The boat ride at sunset is the most magical time to visit. The annual Neermahal Water Festival in August is spectacular."
)
PlaceImage.objects.create(place=p, url="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600", caption="Neermahal rising from Rudrasagar Lake")

print("\n✅ All data seeded successfully!")
print(f"   {Country.objects.count()} country")
print(f"   {City.objects.count()} cities")
print(f"   {Category.objects.count()} categories")
print(f"   {Place.objects.count()} places")
print(f"   {PlaceImage.objects.count()} images")