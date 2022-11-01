import time
import pytest
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider


class Test_RSA_Health(BaseTest):

    @pytest.mark.parametrize("pin,sumvalue,mobileno,selfage,fullname,email,firstname,lastname,dob,income,pan,designation,add1,add2,height,weight,nomfirstname,nomlastname,nomdob", dataProvider.get_data("rsa_health"))
    def test_RSA_Health(self,pin,sumvalue,mobileno,selfage,fullname,email,firstname,lastname,dob,income,pan,designation,add1,add2,height,weight,nomfirstname,nomlastname,nomdob):
        home = HomePage(self.driver)
        healthinsuranepage = home.SelectHealth()
        self.VerifyPresence_PinCodeTextBox()
        healthinsuranepage.landing_page()
        healthinsuranepage.InputPin(pin)
        healthinsuranepage.SelectSum(str(sumvalue))
        healthinsuranepage.InputMobileNo(mobileno)
        insureddetailspage = healthinsuranepage.ClickNext()
        self.VerifyPresence_SelfCheckBox()
        insureddetailspage.landing_page()
        insureddetailspage.SelectMemberSelf()
        self.VerifyPresence_SelfAgeTextBox()
        insureddetailspage.InputAge(selfage)
        time.sleep(2)
        quotespage = insureddetailspage.ClickNext()
        time.sleep(5)
        quotespage.landing_page()
        quotespage.ShareQuotes()
        time.sleep(3)
        quotespage.SelectAllQuotes()
        time.sleep(2)
        quotespage.ClickNext1()
        self.VerifyPresence_NameTextBox()
        quotespage.InputName(fullname)
        quotespage.InputEmail(email)
        quotespage.InputMobileNo(mobileno)
        time.sleep(2)
        quotespage.ClickSubmit()
        time.sleep(2)
        self.VerifyPresence_CloseButton()
        time.sleep(2)
        quotespage.ClickCloseButton()
        time.sleep(2)
        policydetailspage = quotespage.RSAPlanSelect()
        time.sleep(3)
        propdetailspage = policydetailspage.ConfirmTenure()
        policydetailspage.landing_page()
        self.VerifyPresence_FirstNameTextBox()
        propdetailspage.landing_page()
        propdetailspage.InputFirstName(firstname)
        propdetailspage.InputLastName(lastname)
        propdetailspage.InputDOB(dob)
        propdetailspage.SelectPropGender()
        propdetailspage.InputEmailId(email)
        propdetailspage.InputContactNo(mobileno)
        propdetailspage.InputIncome(income)
        propdetailspage.InputPANCard(pan)
        propdetailspage.SelectOccupationDropdown()
        self.VerifyPresence_SelectOccupationOption()
        propdetailspage.SelectOccupation()
        propdetailspage.InputDesignation(designation)
        propdetailspage.SelectMaritalStatusDropdown()
        self.VerifyPresence_MaritalStatusOption()
        propdetailspage.SelectMaritalStatus()
        propdetailspage.SelectEducationDropdown()
        self.VerifyPresence_QualificationOption()
        propdetailspage.SelectQualification()
        propdetailspage.SelectTPANameDropdown()
        self.VerifyPresence_TPANameOption()
        propdetailspage.SelectTPA()
        propdetailspage.InputAdd1(add1)
        propdetailspage.InputAdd2(add2)
        selfdetailspage = propdetailspage.ClickNext()
        self.VerifyPresence_SelfFirstNameTextBox()
        selfdetailspage.landing_page()
        time.sleep(1)
        # selfdetailspage.InputSelfFirstName(firstname)
        # selfdetailspage.InputSelfLastName(lastname)
        # pytest.set_trace()
        # selfdetailspage.InputSelfDOB(dob)
        # selfdetailspage.SelectSelfGender()
        selfdetailspage.InputSelfHeight(height)
        selfdetailspage.InputSelfWeight(weight)
        selfdetailspage.InputSelfDesignation(designation)
        selfdetailspage.InputNomineeFName(nomfirstname)
        selfdetailspage.InputNomineeLName(nomlastname)
        selfdetailspage.InputNomineeDOB(nomdob)
        selfdetailspage.SelectNomineeGender()
        selfdetailspage.SelectNomineeRltnDropdown()
        self.VerifyPresence_NomRelationOption()
        selfdetailspage.SelectNomineeRelation()
        questionariespage = selfdetailspage.ClickNext()
        time.sleep(4)
        questionariespage.landing_page()
        policyreviewpage = questionariespage.ClickNext()
        self.VerifyPresence_NameValidationText()
        policyreviewpage.landing_page()
        proposer_name = policyreviewpage.GetName()
        proposer_email = policyreviewpage.GetEmail()
        proposer_mobno = policyreviewpage.GetPhoneNo()
        try:
            assert proposer_name == fullname
            assert proposer_email == email
            assert int(proposer_mobno) == mobileno
        except Exception as e:
            raise e
        policyreviewpage.FinalSubmit()
        self.VerifyPresence_ShareButton()
        policyreviewpage.SharePolicy()








