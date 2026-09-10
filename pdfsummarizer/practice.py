# import pdfplumber
# import pandas as pd
# with pdfplumber.open("readpdf.pdf") as pdf:
#   pg_number=pdf.pages[0]
#   df=pg_number.extract_tables()
#   #print(df)
#   table=pd.DataFrame(df)
#   print(table.to_string())
#   extracttxt=pg_number.extract_text()
#   print(extracttxt)
#   for index,page in enumerate(pg_number):
   
#     print(f"current page index is {index} and page number is {page}")
#     extracttxt=page.extract_text()
#     print("me extracted",extracttxt)
      
#     if extracttxt=='':
#         print("main khali hun and my inex is ",index)


import textwrap

text = """The Future of Space Exploration

Space exploration has always been one of humanity’s greatest ambitions. For centuries, people looked at the stars and wondered what existed beyond Earth. Today, space exploration is no longer limited to imagination. Scientists, engineers, and space agencies have developed powerful spacecraft, satellites, telescopes, and robots that allow humans to study distant planets and objects. As technology continues to improve, the future of space exploration could bring major discoveries and change our understanding of the universe.

One of the most important goals of future space exploration is returning humans to the Moon. The Moon is relatively close to Earth, which makes it an important location for testing new technologies and preparing for longer missions. Scientists are interested in studying lunar soil, water ice, and the Moon’s environment. Water could become especially valuable because it can potentially be used for drinking, producing oxygen, and creating rocket fuel. A permanent or semi-permanent lunar base could eventually support scientific research and serve as a training ground for missions farther into space.

Mars is another major target for exploration. Mars has fascinated scientists because it shares several characteristics with Earth. It has seasons, polar ice caps, mountains, valleys, and evidence that liquid water existed on its surface in the distant past. Robotic missions have already collected valuable information about the planet. Future missions may send humans to Mars to conduct experiments and search for signs of ancient or existing life. However, traveling to Mars would be extremely difficult. Astronauts would face radiation, isolation, limited resources, and the psychological challenges of spending many months away from Earth.

Robots will continue to play an important role in space exploration. Robotic spacecraft can travel to places that are too dangerous or distant for humans. They can operate for years while collecting photographs, measurements, and samples. Future robots may become more capable because of improvements in artificial intelligence. Instead of depending completely on instructions from Earth, advanced robots could analyze their surroundings and make certain decisions independently. This would be particularly useful when communication delays make direct control difficult.

Space telescopes will also help scientists explore the universe. Telescopes located above Earth's atmosphere can observe objects without many of the distortions caused by the atmosphere. Modern observatories can study distant galaxies, stars, and planets outside our solar system. One of the most exciting areas of research is the search for potentially habitable exoplanets. Scientists have already discovered thousands of planets orbiting other stars. Future telescopes may allow researchers to study the atmospheres of some of these planets and look for chemical signs that could indicate biological activity.

Another important development will be the growth of commercial space companies. In the past, space exploration was largely controlled by national governments. Today, private companies are developing rockets, spacecraft, satellites, and other technologies. Commercial competition can reduce costs and increase the speed of innovation. Companies may eventually provide transportation services to the Moon, operate space stations, or support scientific missions. This could make access to space more common than it is today.

Space tourism is another possibility. Some companies have already developed spacecraft designed to carry private passengers. At present, space tourism remains expensive and accessible to very few people. However, technological improvements could eventually reduce costs. In the future, people might travel to space for short experiences, stay in orbital hotels, or visit commercial space stations. Such activities would require strong safety standards because space remains a dangerous environment.

The development of space resources could also become important. Asteroids contain materials such as metals and other valuable elements. Some scientists and engineers have proposed mining asteroids in the future. The idea is still technically and economically challenging, but advances in robotics could make it more realistic. Resources obtained in space could potentially be used to build equipment without transporting every material from Earth. This could support larger and more ambitious missions.

Despite these opportunities, space exploration has serious challenges. The cost of launching spacecraft remains significant. Space missions require highly reliable equipment because repairs are often impossible once a spacecraft leaves Earth. Radiation can damage electronics and harm astronauts. Long missions require careful management of food, water, oxygen, and waste. Spacecraft also need efficient propulsion systems to travel long distances. Solving these problems will require continued research and international cooperation.

Another concern is the environmental impact of increasing space activity. Thousands of satellites and other objects are currently orbiting Earth. As more spacecraft are launched, the amount of space debris could increase. Small pieces of debris can travel at extremely high speeds and damage or destroy functioning spacecraft. Scientists and space agencies are therefore developing methods to track debris and remove dangerous objects from orbit. Responsible space operations will become increasingly important as human activity beyond Earth grows.

International cooperation will also shape the future of space exploration. No single country has unlimited resources or expertise. Different nations can contribute scientists, engineers, equipment, funding, and launch capabilities. Cooperative missions can reduce costs and increase scientific knowledge. International agreements will also be necessary to address questions about space resources, lunar bases, planetary protection, and the peaceful use of space.

The future may eventually involve humans living and working beyond Earth for long periods. Space stations could become more advanced, and lunar settlements could support scientists and engineers. If technology improves enough, Mars could one day become another location where humans conduct long-term research. However, building permanent settlements would require enormous amounts of planning and resources.

Space exploration also has benefits for people on Earth. Technologies developed for space missions can lead to improvements in communication, navigation, weather forecasting, materials, computing, and medical equipment. Satellites already support many everyday activities, including GPS navigation, telecommunications, television, and environmental monitoring. Continued investment in space technology can therefore have practical benefits far beyond the space industry.

The future of space exploration remains uncertain, but the possibilities are enormous. Humans may discover evidence of life beyond Earth, establish research stations on the Moon, send astronauts to Mars, and develop new ways to travel through space. Robots and artificial intelligence may explore distant worlds that humans cannot reach. Private companies and international partnerships may make space activities more common.

Space exploration is ultimately about understanding our place in the universe. Every new mission can answer some questions while creating new ones. The challenges are difficult, but scientific progress depends on solving difficult problems. As technology develops, humanity will continue pushing the boundaries of what is possible. The next generations may look back at today's space missions as the beginning of a much larger era of exploration.
"""
# print(len(text))
# # Wraps text so every item in the list is a maximum of 500 characters
# chunks = textwrap.wrap(text, width=500) 
# print(chunks)
# print(len(chunks))


# arr=[10,20,30,50,60,70,80,90,100]
# for i in range(0,len(arr),3):
#     print(i)

extracted_txt="i am a complete sentence"
print(len(extracted_txt.split()))


#st.write("new start",extracted_txt)
# splitted_txt=extracted_txt.split()[:1000] 
# st.write("pages splitted",splitted_txt)
# joinedtxt=" ".join(splitted_txt)
# st.write("pages joined",joinedtxt)