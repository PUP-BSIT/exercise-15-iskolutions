from os import system

class TypeMemorizePup:
    def __init__(self):
        self.content = {
            "vision": "A Leading Comprehensive Polytechnic University "
            + "in Asia",
            "mission": "Advance an Inclusive, Equitable, and Globally "
            + "Relevant Polytechnic Education Towards National "
            + "Development",
            "core_values": {
                "i1": "Integrity and Accountability",
                "n": "Nationalism",
                "s": "Sense of Service",
                "p": "Passion for Learning and Innovation",
                "i2": "Inclusivity",
                "r": "Respect for Human Rights and the Environment",
                "e": "Excellence",
                "d": "Democracy"
            },
            "pillars": {
                "pillar1": {
                    "name": "Teaching and Learning",
                    "strategic_goals": {
                        "strategic_goal1": "Innovative Curricula and "
                        + "Instruction",
                        "strategic_goal2": "Empowered Expert, and "
                        + "Productive "
                        + "Faculty Members",
                        "strategic_goal3": "Holistic Student "
                        + "Development"
                    }
                },
                "pillar2": {
                    "name": "Research and Extension",
                    "strategic_goals": {
                        "strategic_goal4": "Intensified Research "
                        + "Innovation, "
                        + "Dissemination and Utilization",
                        "strategic_goal5": "Strengthened Sustainable "
                        + "and Impactful "
                        + "Extension Program",
                        "strategic_goal6": "Expanded Research and "
                        + "Extension "
                        + "Networks with Local, National, and "
                        + "International Partners"
                    }
                },
                "pillar3": {
                    "name": "Internal Governance",
                    "strategic_goals": {
                        "strategic_goal7": "Transformational "
                        + "University Leadership",
                        "strategic_goal8": "Judicious and Ethical "
                        + "Stewardship of Physical and Financial "
                        + "Resources",
                        "strategic_goal9": "Effective and Efficient "
                        + "Human Resources Management",
                        "strategic_goal10": "Excellent Citizen/Client "
                        + "Satisfaction",
                        "strategic_goal11": "Smart Campuses"
                    }
                }
            }
        }
        self.score = 0
        self.attempt = 0

    def test_vision(self):
        print("=================== PUP - VISION ====================")
        self.display_answer_guidelines()
        user_input = input("\nType your answer: ").lower().strip()
        self.attempt += 1

        if user_input == self.content['vision'].lower().strip():
            print("=================================================")
            print("Correct! You got it right!")
            print("=================================================")
            self.score += 1
        else:
            print("\nIncorrect. The correct answer is:")
            print("=================================================")
            print(f"{self.content['vision']}")
            print("=================================================")
            
        print("\nPress Enter to return to Main menu...")
        input()

    def test_mission(self):
        print("================== PUP - MISSION ===================")
        self.display_answer_guidelines()
        user_input = input("\nType your answer: ").lower().strip()
        self.attempt += 1

        if user_input == self.content['mission'].lower().strip():
            print("=================================================")
            print("Correct! You got it right!")
            print("=================================================")
            self.score += 1
        else:
            print("\nIncorrect. The correct answer is:")
            print("=================================================")
            print(f"{self.content['mission']}")
            print("=================================================")
            
        print("\nPress Enter to return to Main menu...")
        input()

    def test_pillars(self):
        print("================== PUP - PILLARS ===================")
        print("Which pillar would you like to test?")
        print("\n1. Teaching and Learning (Pillar 1)")
        print("2. Research and Extension (Pillar 2)")
        print("3. Internal Governance (Pillar 3)")
        print("4. Return to Main Menu")
        print("=====================================================")
        
        try:
            pillar_choice = int(input("\nEnter your choice (1-4): "))
            if pillar_choice == 1:
                self.test_pillar("pillar1", ["strategic_goal1", 
                                             "strategic_goal2", 
                                             "strategic_goal3"])
            elif pillar_choice == 2:
                self.test_pillar("pillar2", ["strategic_goal4", 
                                             "strategic_goal5", 
                                             "strategic_goal6"])
            elif pillar_choice == 3:
                self.test_pillar("pillar3", ["strategic_goal7", 
                                             "strategic_goal8", 
                                             "strategic_goal9",
                                             "strategic_goal10", 
                                             "strategic_goal11"])
            elif pillar_choice == 4:
                return
            else:
                print("Invalid choice. Please select 1-4.")
                print("\nPress Enter to continue...")
                input()
                self.test_pillars()
        except ValueError:
            print("Invalid input. Please enter a valid input.")
            print("\nPress Enter to continue...")
            input()
            self.test_pillars()

    def test_strategic_goals(self, pillar_key, strategic_goal_key):
        pillar_name = self.content["pillars"][pillar_key]["name"]
        print(f"============== PILLAR: {pillar_name} ===============")
        self.display_answer_guidelines()

        for strategic_goal in strategic_goal_key:
            goal_number = strategic_goal.split("strategic_goal")[1]
            display_label = f"SG{goal_number}"
            correct_answer = (self.content["pillars"][pillar_key]
                              ["strategic_goals"][strategic_goal])
            
            print(f"\n{display_label}:")
            user_input = input().lower().strip()
            self.attempt += 1
            
            if user_input == correct_answer.lower().strip():
                print()
                print("=============================================")
                print("Correct! You got it right!")
                print("=============================================")
                self.score += 1
            else:
                print("\nIncorrect. The correct answer is:")
                print("=============================================")
                print(f"{correct_answer}")
                print("=============================================")
        
        print("\nPress Enter to return to Main menu...")
        input()

    def test_core_value(self):
        print("================ PUP - CORE VALUES =================")
        print("\nI N S P I R E D: ")
        
        letters = ["i", "n", "s", "p", "i", "r", "e", "d"]
        core_values = [
            self.content["core_values"]["i1"],  
            self.content["core_values"]["n"],
            self.content["core_values"]["s"],
            self.content["core_values"]["p"],
            self.content["core_values"]["i2"],  
            self.content["core_values"]["r"],
            self.content["core_values"]["e"], 
            self.content["core_values"]["d"]
        ]
        
        for letter, core_value in zip(letters, core_values):
            user_input = input(f"\n{letter.upper()} - ").lower().strip()
            self.attempt += 1
            
            if user_input == core_value.lower().strip():
                print("=============================================")
                print("Correct! You got it right!")
                print("=============================================")
                self.score += 1
            else:
                print("\nIncorrect. The correct answer is:")
                print("=============================================")
                print(f"{core_value}")
                print("=============================================")
        
        print("\nPress Enter to return to Main menu...")
        input()

    def know_pup(self):
        print("==================== KNOW PUP =======================")
        print("\n--- VISION ---")
        print(self.content["vision"])
        
        print("\n--- MISSION ---")
        print(self.content["mission"])
        
        print("\n--- CORE VALUES (INSPIRED) ---")
        print("I - " + self.content["core_values"]["i1"])
        print("N - " + self.content["core_values"]["n"])
        print("S - " + self.content["core_values"]["s"])
        print("P - " + self.content["core_values"]["p"])
        print("I - " + self.content["core_values"]["i2"])
        print("R - " + self.content["core_values"]["r"])
        print("E - " + self.content["core_values"]["e"])
        print("D - " + self.content["core_values"]["d"])
        
        print("\n--- PILLARS AND STRATEGIC GOALS ---")
        for pillar_key, pillar_data in self.content["pillars"].items():
            print(f"\n{pillar_data['name']} ({pillar_key.upper()}):")
            
            for sg_key, sg_value in (pillar_data["strategic_goals"]
                                     .items()):
                sg_number = sg_key.split("strategic_goal")[1]
                print(f"  SG{sg_number}: {sg_value}")
        
        print("\n=================================================")
        print("\nPress Enter to return to Main menu...")
        input()

    def display_answer_guidelines(self):
        print("Note: \n- Answer must be COMPLETE, if not, it is NOT "
              + "counted.")
        print("- It is CASE-INSENSITIVE, meaning, upper and lower "
              + "case are not distinct from each other.")
        print("- INCOMPLETE answer or any probable minor mistakes "
              + "will NOT be counted.")
        print("- Proper comma placement is REQUIRED to be counted")
        print("=====================================================")