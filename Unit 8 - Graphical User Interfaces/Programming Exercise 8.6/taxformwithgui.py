"""
File: taxformwithgui.py
Project 8.6
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and tax rates of
20% for Single
15% for Married
10% for Divorced
"""

from breezypythongui import EasyFrame

STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

        # Label and field for the income
        # (self.incomeField)
        self.addLabel(text="Income", row=0, column=0)
        self.incomeField = self.addFloatField(value="", row=0, column=1)

        # Label and field for the number of dependents
        # (self.depField)
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value="", row=1, column=1)

        # Radio buttons for filing status
        # Button group (self.statusGroup)
        self.statusGroup = self.addRadiobuttonGroup(row=0, column=2, rowspan=3)

        # Option for single (self.single)
        self.single = self.statusGroup.addRadiobutton(text="Single")

        # Option for married (self.married)
        self.married = self.statusGroup.addRadiobutton(text="Married")

        # Option for divorced (self.divorced)
        self.divorced = self.statusGroup.addRadiobutton(text="Divorced")

        self.statusGroup.setSelectedButton(self.single)

        # The compute button
        self.addButton(text="Compute", row=2, column=1, command=self.computeTax)

        # Label and field for the tax
        # (self.taxField)
        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(value="", row=3, column=1)

    # The event handler method for the button
    def computeTax(self):
        grossIncome = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()

        grpSelected = self.statusGroup.getSelectedButton()["text"]

        if grpSelected == "Single":
            TAX_RATE = 0.20
        elif grpSelected == "Married":
            TAX_RATE = 0.15
        elif grpSelected == "Divorced":
            TAX_RATE = 0.10

        taxableIncome = (
            grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
        )

        incomeTax = taxableIncome * TAX_RATE

        self.taxField.setNumber(incomeTax)


def main():
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()
