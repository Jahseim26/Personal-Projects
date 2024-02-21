# Jahseim Merritt
# 04/30/2023
# Comp 163 / section 004
# This program will calculate my grade for comp 163


class GradeScale:
    FILENAMEW = "GradeWeights.txt"
    categories = ["Homework", "Assignments",
                  "Labs", "Assessments", "Midterm", "Final"]
    _gradeWeights: dict()

    def __init__(self, test=False):
        self._gradeWeights = dict()

        if test:
            try:
                self.readWeight(True)
            except FileNotFoundError:
                self.setWeight(True)
            except Exception:
                print("Unknown Error")
            finally:
                print("Test grade weights have been loaded")
        else:
            try:
                self.readWeight()
            except FileNotFoundError:
                self.setWeight()
            except Exception:
                print("Unknown Error")
            finally:
                print("Initial grade weights have been loaded")

    def __str__(self):
        value = ""
        for category, weight in self._gradeWeights.items():
            value += category + " : " + str(weight) + "\n"
        return value

    def readWeight(self, test=False):
        self._gradeWeights.clear()
        file = open(self.FILENAMEW, 'r')

        if test:
            file.close()
            file = open("TestGradeWeights.txt", 'r')

        lines = file.readlines()
        for line in lines:
            item = line.split(",")
            self._gradeWeights.update({item[0]: int(item[1])})
        file.close()

    def setWeight(self, test=False):
        if test:
            for categories in self.categories:
                self._gradeWeights.update({categories: 7})
        else:
            self._gradeWeights.clear()

            for categories in self.categories:
                try:
                    weight = int(
                        input("Enter weight for " + categories + ": "))
                    self._gradeWeights.update({categories: weight})
                except Exception:
                    print("Error")
                finally:
                    print("Try Again")

    def writeWeight(self, test=False):
        if test:
            file = open("TestGradeWeights.txt", 'w')
            for category, weight in self._gradeWeights.items():
                file.write(category + ",5" + "\n")
            file.close()
        else:
            file = open(self.FILENAMEW, 'w')
            for category, weight in self._gradeWeights.items():
                file.write(category + "," + str(weight) + "\n")
            file.close()

    def displayWeights(self):
        value = 1
        for category, weight in self._gradeWeights.items():
            print(str(value) + ") " + category + " : " + str(weight))
            value += 1

    def editWeights(self, category, weight):
        self._gradeWeights.update({category: weight})


class GradeCalculation(GradeScale):
    FILENAMEG = "Grades.txt"

    def __init__(self, test=False):

        if test:
            super().__init__(True)
            self._grades = dict()

            try:
                self.readGrades(True)
            except FileNotFoundError:
                self.setGrades(True)
            except Exception:
                print("Unknown Error")
            finally:
                print("Test grades have been loaded.")
        else:
            super().__init__()
            self._grades = dict()

            try:
                self.readGrades()
            except FileNotFoundError:
                self.setGrades()
            except Exception:
                print("Unknown Error")
            finally:
                print("Initial grades have been loaded.")

    def readGrades(self, test=False):
        self._grades.clear()
        file = open(self.FILENAMEG, 'r')

        if test:
            file.close()
            file = open("TestGrades.txt", 'r')

        lines = file.readlines()
        for line in lines:
            line = line.strip('\n')
            item = line.split(",")
            self._grades.update({item[0]: item[1:]})
        file.close()

    def setGrades(self, test=False):
        self._grades.clear()

        if test:
            for categories in super().categories:
                gradeList = ['100']
                self._grades.update({categories: gradeList})
        else:
            for categories in super().categories:
                gradeList = []
                print("Enter grades for category: " + categories)
                while True:
                    print("Press '-1' to finish category or")
                    try:
                        grade = int(input("Enter grade: "))
                        if grade == -1:
                            self._grades.update({categories: gradeList})
                            break
                        else:
                            gradeList = gradeList + [grade]
                    except Exception:
                        print("Error")
                    finally:
                        print("Try Again")

    def setGrade(self, category):
        gradeList = []
        while True:
            print("Press '-1' to finish or")
            grade = -1
            try:
                grade = int(input("Enter grade: "))
            except Exception:
                print("Error")
            finally:
                print("Try Again")

            if grade == -1:
                self._grades.update({category: gradeList})
                break
            else:
                gradeList = gradeList + [grade]

    def editGrades(self, category, grades):
        self._grades.update({category: grades})

    def displayGrades(self):
        value = 1
        for category, grades in self._grades.items():
            print(f'{str(value)}) {category} : {[str(i) for i in grades]}')
            value += 1

    def writeGrades(self, Test=False):
        if Test:
            file = open("TestGrades.txt", 'w')
            for category, grades in self._grades.items():
                file.write(f'{category},80,90\n')
            file.close()
        else:
            file = open(self.FILENAMEG, 'w')
            for category, grades in self._grades.items():
                file.write(f'{category},{",".join(str(i) for i in grades)}\n')
            file.close()

    def calculateGrades(self):
        finalGrade = 0.0
        for category in super().categories:
            totalPoints = 0
            weight = self._gradeWeights[category]
            grades = self._grades[category]

            for x in grades:
                totalPoints += int(x)

            finalPoints = totalPoints / len(grades)
            finalGrade += finalPoints * (weight / 100)

        print("Weights: ")
        self.displayWeights()
        print("\nGrades: ")
        self.displayGrades()
        print("\nThe final grade is: " + str(finalGrade))


def GradeCalculator():
    print("Welcome to the Grade Calculator Program!")
    gradeCalculator = GradeCalculation()

    while True:
        print("\nMenu 1 Weights")
        option = input(
            "(P)rint (D)isplay (R)ead (W)rite (E)dit (M)anage Grades (Q)uit : ").upper()
        if option == "P":
            print(gradeCalculator._gradeWeights)
        elif option == "R":
            gradeCalculator.readWeight()
            print("File has been successfully read.")
        elif option == "W":
            gradeCalculator.writeWeight()
            print("File has been successfully written.")
        elif option == "D":
            gradeCalculator.displayWeights()
        elif option == "E":
            gradeCalculator.displayWeights()
            try:
                category = int(input("Enter category to edit: "))
                category -= 1
                weight = int(input("Enter new weight for " +
                                   gradeCalculator.categories[category] + ": "))
                gradeCalculator.editWeights(
                    gradeCalculator.categories[category], weight)
            except Exception:
                print("Error")
            finally:
                print("Try Again")
        elif option == "M":
            while True:
                print("\nMenu 2 Grades")
                choice = input(
                    "(P)rint (D)isplay (R)ead (W)rite (E)dit (C)alculate Grades (B)ack : ").upper()
                if choice == "P":
                    print("Test")
                elif choice == "D":
                    gradeCalculator.displayGrades()
                elif choice == "R":
                    gradeCalculator.readGrades()
                    print("File has been successfully read.")
                elif choice == "W":
                    gradeCalculator.writeGrades()
                    print("File has been successfully written.")
                elif choice == "E":
                    gradeCalculator.displayGrades()
                    try:
                        category = int(input("Enter category to edit: "))
                        category -= 1
                        gradeCalculator.setGrade(
                            gradeCalculator.categories[category])
                    except Exception:
                        print("Error")
                    finally:
                        print("Try Again")
                elif choice == "C":
                    gradeCalculator.calculateGrades()
                elif choice == "B":
                    break
        elif option == "Q":
            break
        else:
            print("Invalid Option")


def TestGradeScale():
    while True:
        print("\nHello! Would you like to test: ")
        print("A) ReadWeights")
        print("B) WriteWeights")
        print("C) SetWeights")
        print("D) EditWeights")
        print("E) DisplayWeights")
        print("F) Exit")

        option = input("Select: ").upper()
        print("\n")

        if option == "A":
            TestClass = GradeScale()
            print("Reading From TestGradeWeights.txt")
            print("Expecting:\n1)Homework: 5\n2)Assignments: 5\n3)Labs: 5\n4)Assessments: 5\n5)Midterm: 5\n6)Final: 5")
            TestClass.readWeight(True)

            passing = True
            for value in TestClass._gradeWeights.values():
                if value != 5:
                    passing = False

            if passing:
                print("\nOutput: ")
                TestClass.displayWeights()
                print("\nPass")
            else:
                print("Not Expected Output, File Successfully Read but test failed.")

        elif option == "B":
            TestClass = GradeScale()
            print("Writing To TestGradeWeights.txt")
            print("Expecting to Write:\n1)Homework: 5\n2)Assignments: 5\n3)Labs: 5\n4)Assessments: 5\n5)Midterm: 5\n6)Final: 5")
            TestClass.writeWeight(True)
            TestClass.readWeight(True)

            passing = True
            for value in TestClass._gradeWeights.values():
                if value != 5:
                    passing = False

            if passing:
                print("\nOutput: ")
                TestClass.displayWeights()
                print("\nPass")
            else:
                print("Not Expected Output, File Successfully Read but test failed.")
        elif option == "C":
            TestClass = GradeScale()
            print("Expected to set all Weights to 7")
            TestClass.setWeight(True)
            TestClass.displayWeights()
            print("\nPass")
        elif option == "D":
            TestClass = GradeScale()
            print("Expected to edit the Homework Weight to 6")
            TestClass.editWeights("Homework", 6)
            TestClass.displayWeights()

            if TestClass._gradeWeights["Homework"] == 6:
                print("Pass")
            else:
                print("Fail")
        elif option == "E":
            TestClass = GradeScale()
            TestClass.displayWeights()
            print("Pass")
        elif option == "F":
            print("Exiting")
            break
        else:
            print("Invalid Option\n")


def TestGradeCalculation():
    while True:
        print("\nHello! Would you like to test: ")
        print("A) ReadGrades")
        print("B) WriteGrades")
        print("C) SetGrades/SetGrade")
        print("D) EditGrades")
        print("E) DisplayGrades")
        print("F) CalculateGrades")
        print("G) Exit")

        option = input("Select: ").upper()
        print("\n")

        if option == "A":
            TestClass = GradeCalculation(True)
            print("Reading From TestGrades.txt")
            print(
                "Expecting:\n1)Homework: ['80', '90']\n2)Assignments: ['80', '90']\n3)Labs: ['80', '90']\n4)Assessments: ['80', '90']\n5)Midterm: ['80', '90']\n6)Final: ['80', '90']")
            TestClass.readGrades(True)

            passing = True
            for value in TestClass._grades.values():
                print(value)
                if value != ['80', '90']:
                    passing = False

            if passing:
                print("\nOutput: ")
                TestClass.displayGrades()
                print("\nPass")
            else:
                print("Not Expected Output, File Successfully Read but test failed.")

        elif option == "B":
            TestClass = GradeCalculation(True)
            print("Writing To TestGrades.txt")
            print(
                "Expecting to Write:\n1)Homework: ['80', '90']\n2)Assignments: ['80', '90']\n3)Labs: ['80', '90']\n4)Assessments: ['80', '90']\n5)Midterm: ['80', '90']\n6)Final: ['80', '90']")
            TestClass.writeGrades(True)
            TestClass.readGrades(True)

            passing = True
            for value in TestClass._grades.values():
                if value != ['80', '90']:
                    passing = False

            if passing:
                print("\nOutput: ")
                TestClass.displayGrades()
                print("\nPass")
            else:
                print("Not Expected Output, File Successfully Read but test failed.")
        elif option == "C":
            TestClass = GradeCalculation()
            print("Expected to set all Grades to 100")
            TestClass.setGrades(True)
            TestClass.displayGrades()
            print("\nPass")
        elif option == "D":
            TestClass = GradeCalculation()
            print("Expected to edit the Homework Grade to 20")
            TestClass.editGrades("Homework", ['20'])
            TestClass.displayGrades()

            if TestClass._grades["Homework"] == ['20']:
                print("Pass")
            else:
                print("Fail")
        elif option == "E":
            TestClass = GradeCalculation()
            TestClass.displayGrades()
            print("Pass")
        elif option == "F":
            print("Calculating Grade, Expected output: 40.8")
            TestClass = GradeCalculation(True)
            TestClass.calculateGrades()
        elif option == "G":
            print("Exiting")
            break
        else:
            print("Invalid Option\n")


while True:
    print("\nHello! Would you like to: ")
    print("A) Run Grade Calculator Application")
    print("B) Run GradeScale Class Test Application")
    print("C) Run GradeCalculation Class Test Application")
    print("D) Exit")

    option = input("Select: ").upper()
    print("\n")

    if option == "A":
        GradeCalculator()
    elif option == "B":
        TestGradeScale()
    elif option == "C":
        TestGradeCalculation()
    elif option == "D":
        print("GoodBye!")
        break
    else:
        print("Invalid Option\n")
