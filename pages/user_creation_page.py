from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class UserCreationPage:
    def __init__(self, driver):
        self.driver = driver
        self.heading_add_customer = (By.CSS_SELECTOR, "div[class='row'] h3")  #Add Customer
        self.add_customer_button = (By.CLASS_NAME, 'btn-primary')
        self.customer_name = (By.CSS_SELECTOR, "input[name = 'name']")
        self.customer_s3_folder = (By.CSS_SELECTOR, "input[name = 's3_folder']")
        self.customer_add_s3_folder = (By.CSS_SELECTOR, "input[name = 'additional_s3_folders']")
        self.customer_MAX_SIZE = (By.CSS_SELECTOR, "input[name = 'max_size']")
        self.customer_PANO_MS = (By.CSS_SELECTOR, "input[name = 'pano_max_size']")
        self.Missing_new_alerts = (By.CSS_SELECTOR, "input[name = 'walkaround_alert_num_days_new']")
        self.Missing_used_alerts = (By.CSS_SELECTOR, "input[name = 'walkaround_alert_num_days_used']")
        self.Missing_Max_alerts = (By.CSS_SELECTOR, "input[name = 'walkaround_alert_feed_max_num_photos']")
        self.Exteriors = (By.CSS_SELECTOR, "input[name = 'default_num_images_ec']")
        self.Interiors = (By.CSS_SELECTOR, "input[name = 'default_num_images_i']")
        self.VideoBased = (By.CSS_SELECTOR, "input[name = 'vbwa_num_frames']")
        self.Performance_Report = (By.CSS_SELECTOR, "input[name = 'wwpr_emails']")
        self.Upload_Tracking_checkBox = (By.ID, "notification_emails_checkbox")    #CheckBox
        self.Upload_Tracking_Email = (By.CSS_SELECTOR, "input[name = 'notification_emails']")
        self.WW_PR_Frequency_DDL = (By.CSS_SELECTOR, "select[name = 'wwpr_frequency']")          #Drop Down List
        self.PRR = (By.CSS_SELECTOR, "input[name = 'dpr_emails']")
        self.PhotoR_Frequency_DDL = (By.XPATH, "//select[@name='dpr_frequency']")  #Drop Down List
        # self.PR_Recipients = (By.CSS_SELECTOR, "input[name = 'name']")
        # self.PR_Frequency_DDL = (By.CSS_SELECTOR, "input[name = 'name']")   #Drop Down List
        self.DIR_PR_Email_checkBox = (By.CSS_SELECTOR, "input[name = 'include_dir_in_dpr_email']")
        self.QA_WorkFlow_RD_checkBox = (By.CSS_SELECTOR, "input[name = 'send_qa_workflow_report']")
        self.Lot_service_customers = (By.CSS_SELECTOR, "input[name = 'lot_service_customers']")
        self.Group_Accounts = (By.CSS_SELECTOR, "input[name = 'group_accounts']")
        self.Group_DIR_Recipients = (By.CSS_SELECTOR, "input[name = 'gdir_emails']")
        self.Group_DIR_Frequency_DDL = (By.CSS_SELECTOR, "select[name = 'gdir_frequency']")
        self.Google_Analytics_4_Measurement_ID = (By.CSS_SELECTOR, "input[name = 'ga4_measurement_id']")
        self.CRM_Email = (By.CSS_SELECTOR, "input[name = 'crm_email']")
        self.Additional_Partner_IDS = (By.CSS_SELECTOR, "input[name = 'additional_partner_ids']")
        self.Spin_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_spin_customer']")
        self.Adtech_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_adtech_customer']")
        self.Feature_Tour_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_featuretour_customer']")
        self.Cars_com_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_cars_dot_com_customer']")
        self.CarSales_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_carsales_customer']")
        self.CarBravo_GM_Dealer_Bac_ID = (By.CSS_SELECTOR, "input[name = 'carbravo_gm_bac_id']")
        self.La_Centrale_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_la_centrale_customer']")
        self.PCNA_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_pcna_customer']")
        self.GMF_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_gmf_customer']")
        self.P4C_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_p4c_customer']")
        self.Hide_sold_vehicles_for_partner_checkBox = (By.CSS_SELECTOR, "input[name = 'hide_sold_vehicles_for_partner']")
        self.Enable_Video_Tour_checkBox = (By.CSS_SELECTOR, "input[name = 'video_tour_enabled']")
        self.Enable_Video_Test_Drive_checkBox = (By.CSS_SELECTOR, "input[name = 'enable_videos_test_drive']")
        self.Send_ASC_Formatted_Events_checkBox = (By.CSS_SELECTOR, "input[name = 'send_asc_formatted_events']")
        self.Vindis_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_vindis_customer']")
        self.Autotelex_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_autotelex_customer']")
        self.Use_bounding_box_checkBox = (By.CSS_SELECTOR, "input[name = 'use_bounding_box_stabilization']")
        self.Disable_Carfax_Hotspot_checkBox = (By.CSS_SELECTOR, "input[name = 'carfax_disabled']")
        self.FI_Product_Suite_checkBox = (By.CSS_SELECTOR, "input[name = 'is_fi_customer']")
        self.Enable_Image_Background_checkBox = (By.CSS_SELECTOR, "input[name = 'BACKGROUND_REMOVAL']")
        self.Auction_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_auction_customer']")
        self.ASI_Auction_ID = (By.CSS_SELECTOR, "input[name = 'asi_auction_id']")
        self.CV_Hotspots_Enabled_checkBox = (By.CSS_SELECTOR, "input[name = 'cv_hotspots_enabled']")
        self.CV_Starting_Position_checkBox = (By.CSS_SELECTOR, "input[name = 'cv_starting_position']")
        self.CV_Damage_Tagging_Hotspots_checkBox = (By.CSS_SELECTOR, "input[name = 'cv_damage_tagging_hotspots_enabled']")
        self.Raw_Assets_Available_checkBox = (By.CSS_SELECTOR, "input[name = 'is_feature_highlights_customer']")
        self.Feature_Highlights_customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_feature_highlights_customer']")
        self.Volume_Based_Billing_Customer_checkBox = (By.CSS_SELECTOR, "input[name = 'is_volume_based_billing_customer']")
        self.Streamlined_Damage_Tagging_checkBox = (By.CSS_SELECTOR, "input[name = 'is_simplified_damage_tagging_enabled']")
        self.Enable_Inspection_checkBox = (By.CSS_SELECTOR, "input[name = 'is_inspection_enabled']")
        self.VDP_Sourced_Inventory_checkBox = (By.CSS_SELECTOR, "input[name = 'is_vdp_sourced_inventory']")
        self.Login_email_textBox = (By.CSS_SELECTOR, "input[name = 'email']")
        self.Login_Password_TextBox = (By.CSS_SELECTOR, "input[name = 'password']")
        self.Upload_Tracking_Email_InputBox = (By.CSS_SELECTOR, "input[name = 'notification_emails']")
        self.Enable_Group_I_BE_checkBox = (By.CSS_SELECTOR, "input[name = 'group_abgr_enabled']")
        self.CarSales_DealerID_InputBox = (By.CSS_SELECTOR, "input[name = 'carsales_dealer_id']")
        self.SIREN_number_InputBox = (By.CSS_SELECTOR, "input[name = 'siren_number']")
        self.Vindis_Dealer_ID_InputBox = (By.CSS_SELECTOR, "input[name = 'vindis_dealer_id']")
        self.Autotelex_Dealer_ID_InputBox = (By.CSS_SELECTOR, "input[name = 'autotelex_dealer_id']")
        self.Validation_Row = (By.CSS_SELECTOR, "td[colspan='2']")
        self.save_button = (By.CSS_SELECTOR, "a[id = 'save-customer']")


        self.Auction_Customer_ID_InputBox = (By.CSS_SELECTOR, "asi_auction_id")
        self.Virtual_Booth_checkbox = (By.CSS_SELECTOR, "input[name = 'VIRTUAL_BOOTH']")
        self.Interior_IBE_checkbox = (By.CSS_SELECTOR, "input[name = 'INTERIOR_ABGR']")
        self.Overlays_checkbox = (By.CSS_SELECTOR, "input[name = 'OVERLAYS']")
        self.Interior_CV_Pano_Orientaton_checkbox = (By.CSS_SELECTOR, "input[name = 'cv_hotspots_interior']")
        self.CV_Damage_Tagging_Hotspots_checkbox = (By.CSS_SELECTOR, "input[name = 'cv_damage_tagging_hotspots_enabled']")
        self.pave_checkbox = (By.CSS_SELECTOR, "input[name = 'is_pave_enabled']")
        self.feature_locale_ddl = (By.CSS_SELECTOR, "select[name = 'ft_locale']")

# =================================================Methods to enter data in Input fields ====================================================
    def enter_name(self, name):
        name_field = self.driver.find_element(*self.customer_name)
        name_field.clear()
        name_field.send_keys(name)

    def get_email(self):
        return self.driver.find_element(*self.Login_email_textBox).get_attribute("value")
    def get_password(self):
        return self.driver.find_element(*self.Login_Password_TextBox).get_attribute("value")
    def enter_s3_folder(self, s3_folder):
        s3_folder_field = self.driver.find_element(*self.customer_s3_folder)
        s3_folder_field.clear()
        s3_folder_field.send_keys(s3_folder)

    def enter_max_size(self, max_size):
        max_size_field = self.driver.find_element(*self.customer_MAX_SIZE)
        max_size_field.clear()
        max_size_field.send_keys(max_size)

    def enter_pano_max_size(self, pano_max_size):
        pano_max_size_field = self.driver.find_element(*self.customer_PANO_MS)
        pano_max_size_field.clear()
        pano_max_size_field.send_keys(pano_max_size)

    def enter_missing_WA_a_days_new(self, missing_WA_new):
        new_WA_days_field = self.driver.find_element(*self.Missing_new_alerts)
        new_WA_days_field.clear()
        new_WA_days_field.send_keys(missing_WA_new)

    def enter_missing_WA_a_days_used(self, missing_WA_used):
        used_WA_days_field = self.driver.find_element(*self.Missing_used_alerts)
        used_WA_days_field.clear()
        used_WA_days_field.send_keys(missing_WA_used)


    def enter_missing_WA_a_max_photos(self, missing_WA_max_photos):
        max_WA_photos_field = self.driver.find_element(*self.Missing_used_alerts)
        max_WA_photos_field.clear()
        max_WA_photos_field.send_keys(missing_WA_max_photos)

    def enter_default_ext_WA(self, default_ext_WA):
        default_ext_WA_field = self.driver.find_element(*self.Exteriors)
        default_ext_WA_field.clear()
        default_ext_WA_field.send_keys(default_ext_WA)

    def enter_default_int_WA(self, default_int_WA):
        default_int_WA_field = self.driver.find_element(*self.Interiors)
        default_int_WA_field.clear()
        default_int_WA_field.send_keys(default_int_WA)

    def enter_frames(self, frames):
        frames_field = self.driver.find_element(*self.VideoBased)
        frames_field.clear()
        frames_field.send_keys(frames)

    def enter_WWPR_Report(self, WWPR_Report):
        WWPR_Report_field = self.driver.find_element(*self.Performance_Report)
        WWPR_Report_field.clear()
        WWPR_Report_field.send_keys(WWPR_Report)

    def enter_tracking_email(self, T_email):
        T_email_field = self.driver.find_element(*self.Upload_Tracking_Email)
        T_email_field.clear()
        T_email_field.send_keys(T_email)

    def enter_PRR(self, PRR):
        PRR_field = self.driver.find_element(*self.PRR)
        PRR_field.clear()
        PRR_field.send_keys(PRR)

    def enter_LOT_SC(self, LOT_SC):
        LOT_SC_field = self.driver.find_element(*self.Lot_service_customers)
        LOT_SC_field.clear()
        LOT_SC_field.send_keys(LOT_SC)

    def enter_Group_Account(self, GA):
        GA_field = self.driver.find_element(*self.Group_Accounts)
        GA_field.clear()
        GA_field.send_keys(GA)

    def enter_Group_Dir_R(self, Grop_Dir_R):
        Grop_Dir_R_field = self.driver.find_element(*self.Group_DIR_Recipients)
        Grop_Dir_R_field.clear()
        Grop_Dir_R_field.send_keys(Grop_Dir_R)

    def enter_GA_4_M_ID(self, GA_4_M_ID):
        GA_4_M_ID_field = self.driver.find_element(*self.Google_Analytics_4_Measurement_ID)
        GA_4_M_ID_field.clear()
        GA_4_M_ID_field.send_keys(GA_4_M_ID)

    def enter_CRM_Email(self, CRM_Email):
        CRM_Email_field = self.driver.find_element(*self.CRM_Email)
        CRM_Email_field.clear()
        CRM_Email_field.send_keys(CRM_Email)

    def enter_Add_Partner_IDS(self, name):
        Add_Partner_IDS_field = self.driver.find_element(*self.Additional_Partner_IDS)
        Add_Partner_IDS_field.clear()
        Add_Partner_IDS_field.send_keys(name)

    def enter_CarBravo_G_D_B_ID(self, CarBravo_G_D_B_ID):
        CarBravo_G_D_B_ID_field = self.driver.find_element(*self.CarBravo_GM_Dealer_Bac_ID)
        CarBravo_G_D_B_ID_field.clear()
        CarBravo_G_D_B_ID_field.send_keys(CarBravo_G_D_B_ID)

    def enter_siren_number(self, siren_number):
        siren_number_field = self.driver.find_element(*self.SIREN_number_InputBox)
        siren_number_field.clear()
        siren_number_field.send_keys(siren_number)

    def enter_Carsales_dealer_ID(self, Carsales_dealer_ID):
        Carsales_dealer_ID_field = self.driver.find_element(*self.CarSales_DealerID_InputBox)
        Carsales_dealer_ID_field.clear()
        Carsales_dealer_ID_field.send_keys(Carsales_dealer_ID)

    def enter_Vindis_dealer_ID(self, Vindis_dealer_ID):
        Vindis_dealer_ID_field = self.driver.find_element(*self.Vindis_Dealer_ID_InputBox)
        Vindis_dealer_ID_field.clear()
        Vindis_dealer_ID_field.send_keys(Vindis_dealer_ID)

    def enter_Autotelex_Dealer_ID(self, Autotelex_dealer_ID):
        Autotelex_dealer_ID_field = self.driver.find_element(*self.Autotelex_Dealer_ID_InputBox)
        Autotelex_dealer_ID_field.clear()
        Autotelex_dealer_ID_field.send_keys(Autotelex_dealer_ID)



# ===================================Methods for Checkbox==============================================
    def Click_UploadTracking(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Upload_Tracking_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Upload_Tracking_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_DIR_PR_Email_checkBox(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DIR_PR_Email_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.DIR_PR_Email_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Receive_QA_W_R_Daily(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.QA_WorkFlow_RD_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.QA_WorkFlow_RD_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Spin_Customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Spin_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Spin_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Adtech_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Adtech_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Adtech_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Feature_tour_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Feature_Tour_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Feature_Tour_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Cars_com_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Cars_com_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Cars_com_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_CarSales_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CarSales_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.CarSales_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_la_Centrale_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.La_Centrale_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.La_Centrale_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
    def Click_PCNA_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.PCNA_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.PCNA_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_GMF_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable(self.GMF_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.GMF_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_P4C_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable(self.P4C_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.P4C_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Hide_Sold_vehicle(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Hide_sold_vehicles_for_partner_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Hide_sold_vehicles_for_partner_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Enable_video_tour(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Enable_Video_Tour_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Enable_Video_Tour_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Enable_vehicle_tour_drive(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Enable_Video_Test_Drive_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Enable_Video_Test_Drive_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_send_ASC_formatted_events(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Send_ASC_Formatted_Events_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Send_ASC_Formatted_Events_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Vindis_Customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Vindis_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Vindis_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Autotelex_Customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Autotelex_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Autotelex_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_use_bounding_box(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Use_bounding_box_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Use_bounding_box_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Disable_carfax_hotspot(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DIR_PR_Email_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.DIR_PR_Email_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_F_I_Product_Suites(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.FI_Product_Suite_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.FI_Product_Suite_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Enable_Image_Background(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Enable_Image_Background_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Enable_Image_Background_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Auction_Customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Auction_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Auction_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_CV_Hotspot_Enable(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CV_Hotspots_Enabled_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.CV_Hotspots_Enabled_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)


    def Click_CV_Starting_position(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CV_Starting_Position_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.CV_Starting_Position_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Raw_Assets_Available(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Raw_Assets_Available_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Raw_Assets_Available_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Feature_highlights_customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Feature_Tour_customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Feature_Highlights_customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Volume_Based_Billing_Customer(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Volume_Based_Billing_Customer_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Volume_Based_Billing_Customer_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Streamline_damage_tagging(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Streamlined_Damage_Tagging_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Streamlined_Damage_Tagging_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_Enable_Inspection(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Enable_Inspection_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.Enable_Inspection_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def Click_VDP_Sourced_Inventory(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.VDP_Sourced_Inventory_checkBox)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.VDP_Sourced_Inventory_checkBox)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def click_selector(self):
        try:
            # Wait for the checkbox to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.PhotoR_Frequency_DDL)
            )
            element.click()
        except ElementClickInterceptedException:
            # Scroll the element into view and use JavaScript to click as a fallback
            element = self.driver.find_element(*self.PhotoR_Frequency_DDL)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

#==========================Methods for Selectors==========================================================

    def Select_WWPR_Frequency(self):
        try:
            # Wait until the dropdown is visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.WW_PR_Frequency_DDL))
            # Use JavaScript to click the dropdown
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.WW_PR_Frequency_DDL))
        except TimeoutException:
            print("Dropdown not clickable")
    def get_all_options_WWPRF(self):
        dropdown = Select(self.driver.find_element(*self.WW_PR_Frequency_DDL))
        options = [option.text for option in dropdown.options]
        return options

#Selector2
    def Select_PhotoR_Frequency_DDL(self):
        try:
            # Wait until the dropdown is visible
            WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(self.PhotoR_Frequency_DDL))
            # Use JavaScript to click the dropdown
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.PhotoR_Frequency_DDL))
        except TimeoutException:
            print("Dropdown not clickable")
    def get_all_options_PF(self):
        dropdown = Select(self.driver.find_element(*self.PhotoR_Frequency_DDL))
        options = [option.text for option in dropdown.options]
        return options



# Selector 3
    def Select_Group_DIR_Frequency_DDL(self):
        try:
            # Wait until the dropdown is visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.Group_DIR_Frequency_DDL))
            # Use JavaScript to click the dropdown
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.Group_DIR_Frequency_DDL))
        except TimeoutException:
            print("Dropdown not clickable")
    def get_all_options_Group_DIR_Frequency_DDL(self):
        dropdown = Select(self.driver.find_element(*self.Group_DIR_Frequency_DDL))
        options = [option.text for option in dropdown.options]
        return options

#selector 4

    def Select_feature_locale_ddl(self):
        try:
            # Wait until the dropdown is visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.feature_locale_ddl))
            # Use JavaScript to click the dropdown
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.feature_locale_ddl))
        except TimeoutException:
            print("Dropdown not clickable")

    def get_all_options_feature_locale_ddl(self):
        dropdown = Select(self.driver.find_element(*self.feature_locale_ddl))
        options = [option.text for option in dropdown.options]
        return options

    def Select_option_by_index(self, index):
        dropdown = Select(self.driver.find_element(*self.feature_locale_ddl))
        dropdown.select_by_index(index)

# ============================================Check Validation Row==================================================
    def print_text_from_validation_row(self):
        try:
            element = self.driver.find_element(*self.Validation_Row)
            text = element.text
            if text:
                print(f"Validations Required: {text}")
            else:
                print("No Validations Required.")
        except TimeoutException:
            print("Element not found or not visible.")
# ====================================Click Save Button ===========================================================
    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()






