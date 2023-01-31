# FanFiction

Just provide the series name and this Code will spit out a refined new plot for your amusement


Use

´´´
from FanFictionGenerator import FanFictionGenerator

generator = FanFictionGenerator()
seriesName = "Star Trek"
# seriesName = "friends (tv show)"
story = generator.generate(seriesName)

for i in range(0, 3):
    print("Iteration " + str(i))
    story = generator.improve(seriesName, story)

print("Final Story: " + story)
´´´

Examples:

"friends (tv show)"

The episode begins with Monica and Chandler in their apartment, sitting on the couch and talking. Monica is trying to convince Chandler to let her get a new couch, but Chandler is hesitant because he is worried they can't afford it. Monica argues that the old one is getting worn out and that they should get a new one. Chandler finally agrees and they head out to the furniture store.

Meanwhile, Rachel and Phoebe are out shopping for clothes. Rachel is trying to find a new dress for an upcoming wedding of her old college friend, who she hasn't seen in years. She's excited to catch up with her friend and overwhelmed by the number of styles and colors available. Phoebe is trying to help her, but Rachel is having trouble making up her mind. After trying on a few dresses, Rachel finally decides on a bright pink dress that is perfect for the wedding. 

At the same time, Joey is at Central Perk with Ross. Joey is telling Ross about his latest acting gig for a new sitcom and how he was trying out for the role of the lovable best friend. Ross is happy for him but he's also a bit jealous because Joey is always getting parts and he's having trouble finding work. Joey encourages him to keep trying and Ross agrees, feeling a little more hopeful. 

Monica and Chandler return with the new couch, but they need help getting it inside the cafe. Joey offers to use his truck to transport it and enlist the help of some of the cafe's staff, including Gunther. Gunther had a dolly that he was able to use to move the couch from the store to the cafe with minimal effort. After some effort, they manage to get the couch inside and they all admire it. Joey is impressed and says that it looks really nice. Rachel and Phoebe agree and they all sit down on the new couch to have a cup of coffee. 

After a few minutes, Rachel notices that it's getting late and she has to leave for her friend's wedding. Phoebe and Ross also have to leave, so the group says their goodbyes and Rachel, Phoebe, and Ross all leave. Joey and Chandler stay behind and start talking about the new couch. Chandler is still a bit worried about spending the money, but Joey assures him that it was a good investment.

The episode ends with Chandler and Joey sitting on the new couch, enjoying their coffee and discussing the new purchase.


"Star Trek"

The USS Enterprise was sent on a mission to explore a newly discovered star system in an unexplored part of the galaxy. Upon arriving, the crew soon discovered that the star system was populated by an advanced race of aliens known as the Zetar.

The crew quickly realized that the Zetar were in the midst of a civil war, fueled by a deep-seated religious disagreement about the interpretation of an ancient text. To better understand the ancient Zetarian scripture, the crew immersed themselves in the culture, talked to the locals, and studied the history of the conflict.

After weeks of negotiations, the two sides agreed to a peace treaty, which included a mutual recognition of each side's interpretation of the scripture, an understanding of peaceful coexistence, a joint military force to protect both sides, the opening of trade agreements that allowed for mutual access to resources, technology, and knowledge, and the granting of cultural and religious freedoms such as the freedom to practice their respective religions, the right to travel and explore, and the right to form their own government and laws.

The crew was elated and proud of the successful negotiations and resolution of the conflict. They felt a deep sense of accomplishment, knowing that their efforts had resulted in a peaceful resolution to the conflict. The Zetar thanked them for their efforts and invited them back to their star system for future meetings.
