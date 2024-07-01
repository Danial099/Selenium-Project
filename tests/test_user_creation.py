import json
import uuid
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages import user_creation_page
from pages.customer_list_page import CustomerListPage
from pages.user_creation_page import UserCreationPage
from utils.helpers import read_json, update_user_creation_data_s3Folder, update_user_creation_data_name, save_credentials


@pytest.mark.usefixtures('customer_list_page')

def test_user_creation(driver, user_creation, user_data):

    update_s3Folder = update_user_creation_data_s3Folder('data/user_creation_data.json')
    update_name = update_user_creation_data_name('data/user_creation_data.json')

    user_creation.enter_name(user_data["name"])
    user_creation.enter_s3_folder(user_data["s3_folder"])
    user_creation.enter_pano_max_size(user_data["pano_max_size"])
    user_creation.enter_missing_WA_a_days_new(user_data["walkaround_alert_num_days_new"])
    user_creation.enter_missing_WA_a_days_used(user_data["walkaround_alert_num_days_used"])
    user_creation.enter_missing_WA_a_max_photos(user_data["walkaround_alert_feed_max_num_photos"])
    user_creation.enter_default_ext_WA(user_data["default_num_images_ec"])
    user_creation.enter_default_int_WA(user_data["default_num_images_i"])
    user_creation.enter_frames(user_data["vbwa_num_frames"])
    user_creation.enter_WWPR_Report(user_data["wwpr_emails"])
    user_creation.enter_tracking_email(user_data["notification_emails"])
    user_creation.enter_PRR(user_data["dpr_emails"])
    user_creation.enter_LOT_SC(user_data["lot_service_customers"])
    user_creation.enter_Group_Account(user_data["group_accounts"])
    user_creation.enter_Group_Dir_R(user_data["gdir_emails"])
    user_creation.enter_GA_4_M_ID(user_data["ga4_measurement_id"])
    user_creation.enter_CRM_Email(user_data["crm_email"])
    user_creation.enter_Add_Partner_IDS(user_data["additional_partner_ids"])
    user_creation.enter_CarBravo_G_D_B_ID(user_data["carbravo_gm_bac_id"])
    user_creation.enter_siren_number(user_data["siren_number"])
    user_creation.enter_Vindis_dealer_ID(user_data["vindis_dealer_id"])
    user_creation.enter_Autotelex_Dealer_ID(user_data["autotelex_dealer_id"])
    user_creation.enter_Carsales_dealer_ID(user_data["carsales_dealer_id"])

    # ===================CheckBox===============================#

    user_creation.Click_UploadTracking()
    user_creation.Click_DIR_PR_Email_checkBox()
    user_creation.Click_Receive_QA_W_R_Daily()
    user_creation.Click_Spin_Customer()
    user_creation.Click_Adtech_customer()
    user_creation.Click_Feature_tour_customer()
    user_creation.Click_CarSales_customer()
    user_creation.Click_la_Centrale_customer()
    user_creation.Click_PCNA_customer()
    user_creation.Click_P4C_customer()
    user_creation.Click_Hide_Sold_vehicle()
    user_creation.Click_Enable_video_tour()
    user_creation.Click_Enable_vehicle_tour_drive()
    user_creation.Click_send_ASC_formatted_events()
    user_creation.Click_Vindis_Customer()
    user_creation.Click_Autotelex_Customer()
    user_creation.Click_use_bounding_box()
    user_creation.Click_Disable_carfax_hotspot()
    user_creation.Click_F_I_Product_Suites()
    user_creation.Click_Enable_Image_Background()
    user_creation.Click_Auction_Customer()
    user_creation.Click_CV_Hotspot_Enable()
    user_creation.Click_CV_Starting_position()
    user_creation.Click_Raw_Assets_Available()
    user_creation.Click_Feature_highlights_customer()
    user_creation.Click_Volume_Based_Billing_Customer()
    user_creation.Click_Streamline_damage_tagging()
    user_creation.Click_Enable_Inspection()
    user_creation.Click_VDP_Sourced_Inventory()

    # =========================Selectors=============================
 # Selector1
    user_creation.Select_WWPR_Frequency()
    options_WWPR_Frequency = user_creation.get_all_options_WWPRF()
    expected_options = user_data["WW_PR_Frequency_DDL"]["expected_options"]
    assert options_WWPR_Frequency == expected_options, f"Expected options {expected_options}, but got {options_WWPR_Frequency}"
    user_creation.get_all_options_WWPRF()

    user_creation.click_selector()

    # Selector2
    user_creation.Select_PhotoR_Frequency_DDL()
    options_PhotoR_Frequency_DDL = user_creation.get_all_options_PF()
    expected_options_PR = user_data["PR_Frequency"]["expected_options"]
    assert options_PhotoR_Frequency_DDL == expected_options_PR, f"Expected options {expected_options_PR}, but got {options_PhotoR_Frequency_DDL}"
    print(options_PhotoR_Frequency_DDL)
    # user_creation.get_all_options()

    # Selector 3
    user_creation.Select_Group_DIR_Frequency_DDL()
    options_Group_DIR_Frequency_DDL = user_creation.get_all_options_Group_DIR_Frequency_DDL()
    expected_options_DIR = user_data["Group_DIR_Frequency"]["expected_options"]
    assert options_Group_DIR_Frequency_DDL == expected_options_DIR, f"Expected options {expected_options_DIR}, but got {options_Group_DIR_Frequency_DDL}"
    # user_creation.get_all_options()

    # Selector 4
    user_creation.Select_feature_locale_ddl()
    options_feature_locale_ddl = user_creation.get_all_options_feature_locale_ddl()
    expected_options_feature_locale_ddl = user_data["ft_locale"]["expected_options"]
    assert options_feature_locale_ddl == expected_options_feature_locale_ddl, f"Expected options {expected_options_feature_locale_ddl}, but got {options_feature_locale_ddl}"
    print(options_feature_locale_ddl)
    user_creation.Select_option_by_index(2)

    # =================================checking Email =============================================================================

    name = user_data["name"]
    email_domain = user_data["email_domain"]
    expected_email = f"{name}@{email_domain}"
    actual_email = user_creation.get_email()
    print(actual_email)
    assert actual_email == expected_email, f"Expected email '{expected_email}', but got '{actual_email}'"
    # =============================================password Checking ==================================================================

    actual_password = user_creation.get_password()
    if actual_password:
        print("Password text is present:", actual_password)
    else:
        print("Password text is not present or empty.")

     # ==================================================== Save Credentials ===================================================

    save_credentials(actual_email, actual_password)

    # ===========================================save button method ===============================================================
    expected_url = "https://testautomationchallenge-manager.testenv.impel.io/my-customer/?_acid=3964"
    user_creation.click_save_button()
    WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))

# ================================Customer List ==========================================================================

    customerList = CustomerListPage(driver)
    customerList.Click_user_navBar()
    customerList.Click_user_Logout()
    expected_url_loginpage = "https://testautomationchallenge-manager.testenv.impel.io/login?next=%2F"
    WebDriverWait(driver, 20).until(EC.url_to_be(expected_url_loginpage))
    current_url = driver.current_url
    assert current_url == expected_url_loginpage, f"Expected URL '{expected_url_loginpage}', but got '{current_url}'"




