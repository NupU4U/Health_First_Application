from imports import *
import ctypes
from PIL import Image, ImageTk
from button_front_page import *
from tkinter import ttk
# ctypes.windll.shcore.SetProcessDpiAwareness(1)
key = b"\xcb`\xc2\xb8]\xfb-\x90\xda'\x1f\xfd\x00\x8a\xd0#" 
iv = b'\x10\x8269\xfe\x02e\x00\xfdmR\xfb\xd6\x17\xc2\x17' 

def on_closing():
    global image_filename, entry_text
    if image_filename != None:
        if messagebox.askokcancel("Quit", "Do you want to save the image before quitting?"):
            save_photo()
            if entry_text != None : 
                root.destroy()
        else:
            if (image_filename != None and os.path.isfile(image_filename)):
                os.remove(image_filename)
                root.destroy()   
            else :
                root.destroy()
    else:
        root.destroy() 
def encrypt(key, filename):
    with open(filename, 'rb') as input_file:
        input_data = input_file.read()

    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(input_data)

    with open(filename, 'wb') as enc_file:
        enc_file.write(enc_data)

def decrypt(key, filename):
    with open(filename, 'rb') as enc_file:
        enc_data = enc_file.read()

    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    dec_data = cfb_cipher.decrypt(enc_data)

    output_filename = os.path.splitext(filename)[0] + os.path.splitext(filename)[1]

    with open(output_filename, 'wb') as output_file:
        output_file.write(dec_data)


def on_entry_change(*args):
    global entry_text,clear_flag
    entry_text = entry_var.get()
    # print(entry_text)
    if( clear_flag == 1):
        # print("here")
        entry_text = ""
        entry_var.set("")
        clear_flag = 0 
    
def on_id_change(*args):
    global entry_uhid
    entry_uhid = uhid.get()
    # print(entry_uhid)
def on_sex_change(*args):
    global entry_sex
    entry_sex = sex.get()
    # print(entry_sex)

def on_age_change(*args):
    global entry_age
    entry_age = age.get()
    # print(entry_age)
    
def on_weight_change(*args):
    global entry_weight
    entry_weight = weight.get()
    # print(entry_weight)

def on_bmi_change(*args):
    global entry_bmi
    entry_bmi = bmi.get()
    # print(entry_bmi)

def on_height_change(*args):
    global entry_height
    entry_height = height.get()
    # print(entry_height)

def on_history_dermatological_disease_change(*args):
    global entry_history_dermatological_disease
    entry_history_dermatological_disease = history_dermatological_disease.get()
    # print(entry_history_dermatological_disease)

def on_history_spectacles_change(*args):
    global entry_history_spectacles
    entry_history_spectacles = history_spectacles.get()
    # print(entry_history_spectacles)

def on_blood_pressure_change(*args):
    global entry_blood_pressure
    entry_blood_pressure = blood_pressure.get()
    # print(entry_blood_pressure)

def on_pulse_rate_change(*args):
    global entry_pulse_rate
    entry_pulse_rate = pulse_rate.get()
    # print(entry_pulse_rate)

def on_cardiac_disease_change(*args):
    global entry_cardiac_disease
    entry_cardiac_disease = cardiac_disease.get()
    # print(entry_cardiac_disease)

def on_liver_disease_change(*args):
    global entry_liver_disease
    entry_liver_disease = liver_disease.get()
    # print(entry_liver_disease)

def on_gall_bladder_stones_change(*args):
    global entry_gall_bladder_stones
    entry_gall_bladder_stones = gall_bladder_stones.get()
    # print(entry_gall_bladder_stones)

def on_cancers_change(*args):
    global entry_cancers
    entry_cancers = cancers.get()
    # print(entry_cancers)

def on_lung_change(*args):
    global entry_lung
    entry_lung = lung.get()
    # print(entry_lung)

def on_liver_change(*args):
    global entry_liver
    entry_liver = liver.get()
    # print(entry_liver)

def on_abdominal_change(*args):
    global entry_abdominal
    entry_abdominal = abdominal.get()
    # print(entry_abdominal)

def on_breast_change(*args):
    global entry_breast
    entry_breast = breast.get()
    # print(entry_breast)

def on_brain_change(*args):
    global entry_brain
    entry_brain = brain.get()
    # print(entry_brain)

def on_diabetes_change(*args):
    global entry_diabetes,entry_diabetes_duration
    entry_diabetes = diabetes.get()
    if entry_diabetes == 'Y':
        entry_box_diabetes.config(state='normal')
    if entry_diabetes == 'N':
        entry_box_diabetes.config(state='disabled')
        diabetes_duration.set('')
        entry_diabetes_duration = ""

def on_hypertention_change(*args):
    global entry_hypertention,entry_hypertention_duration
    entry_hypertention = hypertention.get()
    # print(entry_hypertention)
    # print(entry_hypertention)
    if entry_hypertention == 'Y':
        entry_box_hypertention.config(state='normal')
    if entry_hypertention == 'N':
        entry_box_hypertention.config(state='disabled')
        hypertention_duration.set('')
        entry_hypertention_duration = ""

def on_dyslipedemia_change(*args):
    global entry_dyslipedemia,entry_dyslipedemia_duration
    entry_dyslipedemia = dyslipedemia.get()
    # print(entry_dyslipedemia)
    if entry_dyslipedemia == 'Y':
        entry_box_dyslipedemia.config(state='normal')
    if entry_dyslipedemia == 'N':
        entry_box_dyslipedemia.config(state='disabled')
        dyslipedemia_duration.set('')
        entry_dyslipedemia_duration = ""


def on_hypothyroid_change(*args):
    global entry_hypothyroid, entry_hypothyroid_duration
    entry_hypothyroid = hypothyroid.get()
    # print(entry_hypothyroid)
    if entry_hypothyroid == 'Y':
        entry_box_hypothyroid.config(state='normal')
    if entry_hypothyroid == 'N':
        entry_box_hypothyroid.config(state='disabled')
        hypothyroid_duration.set('')
        entry_hypothyroid_duration = ""

def on_hyperthyroid_change(*args):
    global entry_hyperthyroid,entry_hyperthyroid_duration
    entry_hyperthyroid = hyperthyroid.get()
    # print(entry_hyperthyroid)
    if entry_hyperthyroid == 'Y':
        entry_box_hyperthyroid.config(state='normal')
    if entry_hyperthyroid == 'N':
        entry_box_hyperthyroid.config(state='disabled')
        hyperthyroid_duration.set('')
        entry_hyperthyroid_duration = ""

def on_cardiac_change(*args):
    global entry_cardiac,entry_cardiac_duration
    entry_cardiac = cardiac.get()
    # print(entry_cardiac)
    if entry_cardiac == 'Y':
        entry_box_cardiac.config(state='normal')
    if entry_cardiac == 'N':
        entry_box_cardiac.config(state='disabled')
        cardiac_duration.set('')
        entry_cardiac_duration = ""

def on_respiratory_change(*args):
    global entry_respiratory,entry_respiratory_duration
    entry_respiratory = respiratory.get()
    # print(entry_respiratory)
    if entry_respiratory == 'Y':
        entry_box_respiratory.config(state='normal')
    if entry_respiratory == 'N':
        entry_box_respiratory.config(state='disabled')
        respiratory_duration.set('')
        entry_respiratory_duration = ""

def on_renal_change(*args):
    global entry_renal, entry_renal_duration
    entry_renal = renal.get()
    # print(entry_renal)
    if entry_renal == 'Y':
        entry_box_renal.config(state='normal')
    if entry_renal == 'N':
        entry_box_renal.config(state='disabled')
        renal_duration.set('')
        entry_renal_duration = ""
        
def on_chronic_liver_disease_change(*args):
    global entry_chronic_liver_disease
    entry_chronic_liver_disease = chronic_liver_disease.get()
    # print(entry_chronic_liver_disease)

def on_ethanol_change(*args):
    global entry_ethanol
    entry_ethanol = ethanol.get()
    # print(entry_ethanol)

def on_bleed_change(*args):
    global entry_bleed
    entry_bleed = bleed.get()
    # print(entry_bleed)

def on_nash_change(*args):
    global entry_nash
    entry_nash = nash.get()
    # print(entry_nash)

def on_hepatitis_b_change(*args):
    global entry_hepatitis_b
    entry_hepatitis_b = hepatitis_b.get()
    # print(entry_hepatitis_b)

def on_encephalopathy_change(*args):
    global entry_encephalopathy
    entry_encephalopathy = encephalopathy.get()
    # print(entry_encephalopathy)

def on_hepatitis_c_change(*args):
    global entry_hepatitis_c
    entry_hepatitis_c = hepatitis_c.get()
    # print(entry_hepatitis_c)
    
def on_autoimmune_change(*args):
    global entry_autoimmune
    entry_autoimmune = autoimmune.get()
    # print(entry_autoimmune)

def on_ascites_change(*args):
    global entry_ascites
    entry_ascites = ascites.get()
    # print(entry_ascites)

def on_upper_gi_change(*args):
    global entry_upper_gi_bleed
    entry_upper_gi_bleed = upper_gi_bleed.get()
    # print(entry_upper_gi_bleed)

def on_jaundice_change(*args):
    global entry_jaundice
    entry_jaundice = jaundice.get()
    # print(entry_jaundice)

def on_hepatic_change(*args):
    global entry_hepatic
    entry_hepatic = hepatic.get()
    # print(entry_hepatic)

def on_hcc_change(*args):  
    global entry_hcc
    entry_hcc = hcc.get()
    # print(entry_hcc)
    
def on_hba1c_change(*args):
    global entry_hba1c
    entry_hba1c = hba1c.get()
    # print(entry_hba1c)

def on_endoscopy_change(*args):
    global entry_endoscopy
    entry_endoscopy = endoscopy.get()
    # print(entry_endoscopy)

def on_bilirubin_change(*args):
    global entry_bilirubin
    entry_bilirubin = bilirubin.get()
    # print(entry_bilirubin)

def on_diabetes_duration_change(*args):
    global entry_diabetes_duration
    entry_diabetes_duration = diabetes_duration.get()
    # print(entry_diabetes_duration)

def on_hypertention_duration_change(*args):
    global entry_hypertention_duration
    entry_hypertention_duration = hypertention_duration.get()
    # print(entry_hypertention_duration)

def on_dyslipedemia_duration_change(*args):
    global entry_dyslipedemia_duration
    entry_dyslipedemia_duration = dyslipedemia_duration.get()
    # print(entry_dyslipedemia_duration)

def on_hypothyroid_duration_change(*args):
    global entry_hypothyroid_duration
    entry_hypothyroid_duration = hypothyroid_duration.get()
    # print(entry_hypothyroid_duration)

def on_hyperthyroid_duration_change(*args):
    global entry_hyperthyroid_duration
    entry_hyperthyroid_duration = hyperthyroid_duration.get()
    # print(entry_hyperthyroid_duration)
    
def on_cardiac_duration_change(*args):
    global entry_cardiac_duration
    entry_cardiac_duration = cardiac_duration.get()
    # print(entry_cardiac_duration)

def on_respiratory_duration_change(*args):
    global entry_respiratory_duration
    entry_respiratory_duration = respiratory_duration.get()
    # print(entry_respiratory_duration)

def on_renal_duration_change(*args):
    global entry_renal_duration
    entry_renal_duration = renal_duration.get()
    # print(entry_renal_duration)


def on_heamoglobin_change(*args):
    global entry_heamoglobin
    entry_heamoglobin = heamoglobin.get()
    # print(entry_heamoglobin)
    
def on_creatinine_change(*args):
    global entry_creatinine
    entry_creatinine = creatinine.get()
    # print(entry_creatinine)

def on_platelet_count_change(*args):
    global entry_platelet_count
    entry_platelet_count = platelet_count.get()
    # print(entry_platelet_count)
    
def on_urea_change(*args):
    global entry_urea
    entry_urea = urea.get()
    # print(entry_urea)

def on_fasting_blood_sugar_change(*args):
    global entry_fasting_blood_sugar
    entry_fasting_blood_sugar = fasting_blood_sugar.get()
    # print(entry_fasting_blood_sugar)
    
def on_sodium_change(*args):
    global entry_sodium
    entry_sodium = sodium.get()
    # print(entry_sodium)
    
def on_postprandial_blood_sugar_change(*args):
    global entry_postprandial_blood_sugar
    entry_postprandial_blood_sugar = postprandial_blood_sugar.get()
    # print(entry_postprandial_blood_sugar)

def on_fibroscan_change(*args):
    global entry_fibroscan
    entry_fibroscan = fibroscan.get()
    # print(entry_fibroscan)

def limit_input_length(P):
    if len(P) <= 20:
        return True
    else:
        return False
    
def clear_all(*args): 
    global entry_var, uhid,age,weight,bmi,height,history_dermatological_disease,history_spectacles,blood_pressure,pulse_rate,cardiac_disease,liver_disease,gall_bladder_stones,cancers,liver,lung,abdominal,breast,brain,diabetes,hypertention,dyslipedemia,hypothyroid,hyperthyroid,cardiac,respiratory,renal,diabetes_duration,hypertention_duration,dyslipedemia_duration,hypothyroid_duration,hypertention_duration,cardiac_duration,respiratory_duration,renal_duration,bilirubin
    sex.set(None)
    entry_var.set("")
    uhid.set("")
    age.set("")
    weight.set("")
    bmi.set("")
    height.set("")
    history_dermatological_disease.set(None)
    history_spectacles.set(None)
    blood_pressure.set("")
    pulse_rate.set("")
    cardiac_disease.set(None)
    liver_disease.set(None)
    gall_bladder_stones.set(None)
    cancers.set(None)
    lung.set(None)
    liver.set(None)
    abdominal.set(None)
    breast.set(None)
    brain.set(None)
    diabetes.set(None)
    hypertention.set(None)
    dyslipedemia.set(None)
    hypothyroid.set(None)
    hyperthyroid.set(None)
    cardiac.set(None)
    respiratory.set(None)
    renal.set(None)
    diabetes_duration.set("")
    hypertention_duration.set("")
    dyslipedemia_duration.set("")
    hypothyroid_duration.set("")
    hyperthyroid_duration.set("")
    cardiac_duration.set("")
    respiratory_duration.set("")
    renal_duration.set("")
    chronic_liver_disease.set(None)
    ethanol.set(None)
    bleed.set(None)
    nash.set(None)
    hepatitis_b.set(None)
    encephalopathy.set(None)
    hepatitis_c.set(None)
    autoimmune.set(None)
    ascites.set(None)
    upper_gi_bleed.set(None)
    jaundice.set(None)
    hepatic.set(None)
    hcc.set(None)
    heamoglobin.set("")
    platelet_count.set("")
    fasting_blood_sugar.set("")
    postprandial_blood_sugar.set("")
    creatinine.set("")
    urea.set("")
    sodium.set("")
    fibroscan.set("")
    hba1c.set(None)
    endoscopy.set(None)
    bilirubin.set("")
    
def crop_image(image_path, save_path):
    global mouse_pressed, photo, image_label, image_filename
    img_dup = None
    starting_x = starting_y = ending_x = ending_y = -1
    if image_filename == None:
        messagebox.showerror("Error", "No image captured")
        return
    def mousebutton(event, x, y, flags, param):
        global mouse_pressed 
        nonlocal starting_x, starting_y, img_dup

        if event == cv2.EVENT_LBUTTONDOWN:
            mouse_pressed = True
            starting_x, starting_y = x, y
            img_dup = np.copy(img)
        elif event == cv2.EVENT_MOUSEMOVE:
            if mouse_pressed:
                img_dup = np.copy(img)
                cv2.rectangle(img_dup, (starting_x, starting_y), (x, y), (0, 255, 0), 1)
        elif event == cv2.EVENT_LBUTTONUP:
            nonlocal ending_x, ending_y
            mouse_pressed = False
            ending_x, ending_y = x, y

    img = cv2.imread(image_filename)
    img_dup = np.copy(img)
    
    cv2.namedWindow('Press Enter to CROP')
    cv2.setMouseCallback('Press Enter to CROP', mousebutton)
    while True:
        cv2.imshow('Press Enter to CROP', img_dup)
        k = cv2.waitKey(1)
        if k == 13:  # Press Enter key to exit
            if starting_y > ending_y:
                starting_y, ending_y = ending_y, starting_y
            if starting_x > ending_x:
                starting_x, ending_x = ending_x, starting_x
            if ending_y - starting_y > 0 and ending_x - starting_x > 0:
                image = img[starting_y:ending_y, starting_x:ending_x]
                img_dup = np.copy(image)
                break
            else:
                image = img
                img_dup = np.copy(image)
                break

    cv2.imwrite(save_path, img_dup)  
    cv2.destroyAllWindows()
    image = Image.open(image_filename)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)

    return confirmation

def headers_match(expected, actual):
    return all(x == y for x, y in zip(expected, actual))
def undo():
    global image_label, photo, image_filename, image_copy, frame
    if image_filename == None:
        messagebox.showerror("Error", "No image captured")
        return
    photo = ImageTk.PhotoImage(image_copy)
    image_label.config(image=photo)
    cv2.imwrite(image_filename,frame )  # Save the cropped image to the specified save_pat
    return
def insert_data_to_sql_database(host, user, password, database, dataframee):
    try:
        dataframe = dataframee
        dataframe = dataframe.fillna('')

        conn = msql.connect(host=host, user=user, password=password, database=database)
        if conn.is_connected():
            cursor = conn.cursor()
            print("You're connected to the database")

            # Check if the table exists
            cursor.execute("SHOW TABLES LIKE 'imagefile_data'")
            table_exists = cursor.fetchone()

            if not table_exists:
                print('Creating table....')
                # Modify the table creation SQL statement to include the additional columns
                cursor.execute("""
                    CREATE TABLE imagefile_data (
                        PatientID varchar(255), 
                        ImageFilename varchar(255), 
                        ImageSizeInBytes INT, 
                        CaptureTime varchar(255), 
                        Sex varchar(10), 
                        UHID varchar(20), 
                        Age varchar(20), 
                        Weight_kgs varchar(20), 
                        BMI varchar(20), 
                        Height_cms varchar(20), 
                        History_of_dermatological_disease varchar(20), 
                        History_of_spectacle_use varchar(20), 
                        Blood_Pressure varchar(20), 
                        Pulse_Rate varchar(20), 
                        Cardiac_Disease_fh varchar(20), 
                        Liver_disease_fh varchar(20), 
                        Gall_bladder_stones_fh varchar(20), 
                        Cancers_fh varchar(20), 
                        Lung_fh varchar(20), 
                        Liver_fh varchar(20), 
                        Abdomen_fh varchar(20), 
                        Breast_fh varchar(20), 
                        Brain_fh varchar(20),
                        Diabetes varchar(20),
                        Diabetes_Duration varchar(20),
                        Hypertention varchar(20),
                        Hypertention_Duration varchar(20),
                        Dyslipidemia varchar(20),
                        Dyslipidemia_Duration varchar(20),
                        Hypothyroid varchar(20),
                        Hypothyroid_Duration varchar(20),
                        Hyperthyroid varchar(20),
                        Hyperthyroid_Duration varchar(20),
                        Cardiac_Disease varchar(20),
                        Cardiac_Disease_Duration varchar(20),
                        Respiratory_disease varchar(20),
                        Respiratory_disease_Duration varchar(20),
                        Renal_disease varchar(20),
                        Renal_disease_Duration varchar(20),
                        Chronic_Liver_Disease varchar(20),
                        Ethanol varchar(20),
                        bleed_Bleeder varchar(20),
                        NASH varchar(20),
                        Hepatitis_B varchar(20),
                        Encephalopathy varchar(20),
                        Hepatitis_C varchar(20),
                        Autoimmune varchar(20),
                        Ascites varchar(20),
                        Upper_GI varchar(20),
                        Jaundice varchar(20),
                        Hepatic varchar(20),
                        HCC varchar(20),
                        Heamoglobin varchar(20),
                        Creatinine varchar(20),
                        Platelet_Count varchar(20),
                        Urea varchar(20),
                        FBS varchar(20),
                        Sodium varchar(20),
                        PPG varchar(20),
                        Fibroscan varchar(20),
                        HbA1c varchar(20), 
                        Endoscopy varchar(20),
                        Bilirubin varchar(20) 
                    );
                """)
                print("Table is created....")

            sql_update = '''
                UPDATE imagefile_data 
                SET PatientID = %s, 
                    ImageSizeInBytes = %s, 
                    CaptureTime = %s, 
                    Sex = %s, 
                    UHID = %s, 
                    Age = %s, 
                    Weight_kgs = %s, 
                    BMI = %s, 
                    Height_cms = %s, 
                    History_of_dermatological_disease = %s, 
                    History_of_spectacle_use = %s, 
                    Blood_Pressure = %s, 
                    Pulse_Rate = %s, 
                    Cardiac_Disease_fh = %s, 
                    Liver_disease_fh = %s, 
                    Gall_bladder_stones_fh = %s, 
                    Cancers_fh = %s, 
                    Lung_fh = %s, 
                    Liver_fh = %s, 
                    Abdomen_fh = %s, 
                    Breast_fh = %s, 
                    Brain_fh = %s,
                    Diabetes = %s,
                    Diabetes_Duration = %s,
                    Hypertention = %s,
                    Hypertention_Duration = %s,
                    Dyslipidemia = %s,
                    Dyslipidemia_Duration = %s,
                    Hypothyroid = %s,
                    Hypothyroid_Duration = %s,
                    Hyperthyroid = %s,
                    Hyperthyroid_Duration = %s,
                    Cardiac_Disease = %s,
                    Cardiac_Disease_Duration = %s,
                    Respiratory_disease = %s,
                    Respiratory_disease_Duration = %s,
                    Renal_disease = %s,
                    Renal_disease_Duration = %s,
                    Chronic_Liver_Disease = %s,
                    Ethanol = %s,
                    bleed_Bleeder = %s,
                    NASH = %s,
                    Hepatitis_B = %s,
                    Encephalopathy = %s,
                    Hepatitis_C = %s,
                    Autoimmune = %s,
                    Ascites = %s,
                    Upper_GI = %s,
                    Jaundice = %s,
                    Hepatic = %s,
                    HCC = %s,
                    Heamoglobin= %s,
                    Creatinine = %s,
                    Platelet_Count = %s,
                    Urea = %s,
                    FBS = %s,
                    Sodium = %s,
                    PPG = %s,
                    Fibroscan = %s,
                    HbA1c = %s, 
                    Endoscopy = %s,
                    Bilirubin = %s
                WHERE ImageFilename = %s
            '''

            sql_insert = '''
                INSERT INTO imagefile_data (
                    PatientID, ImageFilename, ImageSizeInBytes, CaptureTime, Sex, UHID, Age, Weight_kgs, BMI, Height_cms, 
                    History_of_dermatological_disease, History_of_spectacle_use, Blood_Pressure, Pulse_Rate, Cardiac_Disease_fh, 
                    Liver_disease_fh, Gall_bladder_stones_fh, Cancers_fh, Lung_fh, Liver_fh, Abdomen_fh, Breast_fh, Brain_fh,
                    Diabetes, Diabetes_Duration, Hypertention, Hypertention_Duration, Dyslipidemia, Dyslipidemia_Duration, 
                    Hypothyroid, Hypothyroid_Duration, Hyperthyroid, Hyperthyroid_Duration, Cardiac_Disease, 
                    Cardiac_Disease_Duration, Respiratory_disease, Respiratory_disease_Duration, Renal_disease, 
                    Renal_disease_Duration, Chronic_Liver_Disease, Ethanol,bleed_Bleeder, NASH, Hepatitis_B, Encephalopathy,
                    Hepatitis_C, Autoimmune, Ascites, Upper_GI, Jaundice, Hepatic, HCC, Heamoglobin, Creatinine,
                    Platelet_Count, Urea, FBS, Sodium, PPG, Fibroscan , HbA1c, Endoscopy, Bilirubin 
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            for i, row in dataframe.iterrows():
                # Check if the record exists
                cursor.execute("SELECT * FROM imagefile_data WHERE ImageFilename = %s", (row['Image Filename'],))
                existing_record = cursor.fetchone()

                if existing_record:
                    # Use the UPDATE statement
                    cursor.execute(sql_update, (
                        row['Patient ID'], row['Image Size (bytes)'], row['Capture Time'], row['Sex'], row['UHID'], 
                        row['Age'], row['Weight_kgs'], row['BMI'], row['Height_cms'], row['History_of_dermatological_disease'], 
                        row['History_of_spectacle_use'], row['Blood_Pressure'], row['Pulse_Rate'], row['Cardiac_Disease_fh'], 
                        row['Liver_disease_fh'], row['Gall_bladder_stones_fh'], row['Cancers_fh'], row['Lung_fh'], row['Liver_fh'], 
                        row['Abdomen_fh'], row['Breast_fh'], row['Brain_fh'], row['Diabetes'], row['Diabetes_Duration'], 
                        row['Hypertention'], row['Hypertention_Duration'], row['Dyslipidemia'], row['Dyslipidemia_Duration'], 
                        row['Hypothyroid'], row['Hypothyroid_Duration'], row['Hyperthyroid'], row['Hyperthyroid_Duration'], 
                        row['Cardiac_Disease'], row['Cardiac_Disease_Duration'], row['Respiratory_disease'], 
                        row['Respiratory_disease_Duration'], row['Renal_disease'], row['Renal_disease_Duration'],
                        row['Chronic_Liver_Disease'], row['Ethanol'],row['bleed_Bleeder'], row['NASH'], row['Hepatitis_B'], row['Encephalopathy'],
                        row['Hepatitis_C'], row['Autoimmune'], row['Ascites'], row['Upper_GI'], row['Jaundice'], row['Hepatic'], row['HCC'], row['Heamoglobin'], row['Creatinine'],
                        row['Platelet_Count'], row['Urea'], row['FBS'], row['Sodium'], row['PPG'], row['Fibroscan'] , row['HbA1c'], row['Endoscopy'], row['Bilirubin'], row['Image Filename']
                    ))
                    print("Record updated")
                else:
                    # Use the INSERT statement
                    cursor.execute(sql_insert, (
                        row['Patient ID'], row['Image Filename'], row['Image Size (bytes)'], row['Capture Time'], row['Sex'], 
                        row['UHID'], row['Age'], row['Weight_kgs'], row['BMI'], row['Height_cms'], 
                        row['History_of_dermatological_disease'], row['History_of_spectacle_use'], row['Blood_Pressure'], 
                        row['Pulse_Rate'], row['Cardiac_Disease_fh'], row['Liver_disease_fh'], row['Gall_bladder_stones_fh'], 
                        row['Cancers_fh'], row['Lung_fh'], row['Liver_fh'], row['Abdomen_fh'], row['Breast_fh'], row['Brain_fh'],
                        row['Diabetes'], row['Diabetes_Duration'], row['Hypertention'], row['Hypertention_Duration'], 
                        row['Dyslipidemia'], row['Dyslipidemia_Duration'], row['Hypothyroid'], row['Hypothyroid_Duration'], 
                        row['Hyperthyroid'], row['Hyperthyroid_Duration'], row['Cardiac_Disease'], 
                        row['Cardiac_Disease_Duration'], row['Respiratory_disease'], row['Respiratory_disease_Duration'], 
                        row['Renal_disease'], row['Renal_disease_Duration'], row['Chronic_Liver_Disease'], row['Ethanol'],row['bleed_Bleeder'], row['NASH'], row['Hepatitis_B'], row['Encephalopathy'],
                        row['Hepatitis_C'], row['Autoimmune'], row['Ascites'], row['Upper_GI'], row['Jaundice'], row['Hepatic'], row['HCC'], row['Heamoglobin'], row['Creatinine'],
                        row['Platelet_Count'], row['Urea'], row['FBS'], row['Sodium'], row['PPG'], row['Fibroscan'] , row['HbA1c'], row['Endoscopy'], row['Bilirubin']
                    ))
                    print("Record inserted")

            conn.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)

def show_captured_image(event):
    global image_label, photo, image_filename, image_copy, frame, ret , current_time, flag_saved
    if flag_saved == True:
        image_filename = None
    else :
        if image_filename != None:
            os.remove(image_filename)
            image_filename = None
    ret, frame = camera_capture.read()    
    if ret:
        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        if not os.path.exists("captured_images"):
            os.makedirs("captured_images")
        image_filename = f"captured_images/captured_image_{current_time}.jpeg"
        
        cv2.imwrite(image_filename, frame)
        image = Image.open(image_filename)
        image_copy = image.copy()
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.bind("<Configure>",  image_label.place(relx=0.5, rely=0.5, anchor='center'))
def save_photo():
    global _flag, file_path, confirmation, image_filename, frame_captured_image, image_label, label, camera_feed_label, photo, ret, current_time, entry_text, mouse_pressed, image_copy, captured_frame, frame, flag_saved

    expected_headers = ["Patient ID", "Image Filename", "Image Size (bytes)", "Capture Time", "Sex", "UHID", "Age", "Weight_kgs", "BMI", "Height_cms", "History_of_dermatological_disease", "History_of_spectacle_use", "Blood_Pressure", "Pulse_Rate", "Cardiac_Disease_fh", "Liver_disease_fh", "Gall_bladder_stones_fh", "Cancers_fh", "Lung_fh", "Liver_fh", "Abdomen_fh", "Breast_fh", "Brain_fh", "Diabetes", "Diabetes_Duration", "Hypertention", "Hypertention_Duration", "Dyslipidemia", "Dyslipidemia_Duration", "Hypothyroid", "Hypothyroid_Duration", "Hyperthyroid", "Hyperthyroid_Duration", "Cardiac_Disease", "Cardiac_Disease_Duration", "Respiratory_disease", "Respiratory_disease_Duration", "Renal_disease", "Renal_disease_Duration"]

    if entry_text is None:
        messagebox.showerror("Error", "Enter a valid Patient ID")
        return

    if ret:
        confirmation = messagebox.askquestion("Save Image", "Do you want to save the image?")
        if confirmation == "yes":
            # Obtain the patient ID from the entry_text
            patient_id = entry_text
            sex_val = entry_sex
            uhid_val = entry_uhid
            age_val = entry_age
            wt_val = entry_weight
            bmi_val = entry_bmi
            ht_val = entry_height
            history_dermatological_disease_val = entry_history_dermatological_disease
            history_spectacle_use_val = entry_history_spectacles
            bp_val = entry_blood_pressure
            pr_val = entry_pulse_rate
            cd_val = entry_cardiac_disease
            ld_val = entry_liver_disease
            gbs_val = entry_gall_bladder_stones
            cancers_val = entry_cancers
            lung_val = entry_lung
            liver_val = entry_liver
            abdomen_val = entry_abdominal
            breast_val = entry_breast
            brain_val = entry_brain
            diabetes_val = entry_diabetes
            diabetes_duration_val = entry_diabetes_duration
            hypr_val = entry_hypertention
            hypr_dr_val = entry_hypertention_duration
            dyslipedemia_val = entry_dyslipedemia
            dyslipedemia_dr_val = entry_dyslipedemia_duration
            hypothyroid_val = entry_hypothyroid
            hypothyroid_dr_val = entry_hypothyroid_duration
            hyperthyroid_val = entry_hyperthyroid
            hyperthyroid_dr_val = entry_hyperthyroid_duration
            cardiac_disease_val = entry_cardiac
            cardiac_disease_dr_val = entry_cardiac_duration
            respiratory_val = entry_respiratory
            respiratory_dr_val = entry_respiratory_duration
            renal_val = entry_renal
            renal_dr_val = entry_renal_duration
            chronic_liver_disease_val = entry_chronic_liver_disease
            ethanol_val = entry_ethanol
            bleed_Bleeder_val = entry_bleed
            nash_val = entry_nash
            hepatitis_b_val = entry_hepatitis_b
            encephalopathy_val = entry_encephalopathy   
            hepatitis_c_val = entry_hepatitis_c
            autoimmune_val = entry_autoimmune
            ascites_val = entry_ascites
            upper_gi_bleed_val = entry_upper_gi_bleed
            jaundice_val = entry_jaundice
            hepatic_val = entry_hepatic
            hcc_val = entry_hcc
            heamoglobin_val = entry_heamoglobin
            creatinine_val = entry_creatinine
            platelet_count_val = entry_platelet_count
            urea_val = entry_urea
            fasting_blood_sugar_val = entry_fasting_blood_sugar
            sodium_val = entry_sodium
            postprandial_blood_sugar_val = entry_postprandial_blood_sugar
            fibroscan_val = entry_fibroscan
            hba1c_val = entry_hba1c
            endoscopy_val = entry_endoscopy
            bilirubin_val = entry_bilirubin
            
            # Create the updated image filename with the patient ID as a prefix
            updated_image_filename = f"captured_images/{patient_id}_{os.path.basename(image_filename)}"

            # Rename the file with the updated name
            os.rename(image_filename, updated_image_filename)

            image_size = os.path.getsize(updated_image_filename)

            csv_filename = 'captured_image_details.csv'
            is_empty_csv = not os.path.isfile(csv_filename) or os.stat(csv_filename).st_size == 0

            # Read the existing header row (if it exists)
            header_row = []
            if not is_empty_csv:
                with open(csv_filename, "r") as csvfile:
                    csv_reader = csv.reader(csvfile)
                    header_row = next(csv_reader, None)

            with open(csv_filename, "a", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)

                if is_empty_csv or not headers_match(expected_headers, header_row):
                    csvfile.seek(0)  # Move to the beginning of the file
                    csvfile.truncate()  # Clear the file
                    csv_writer.writerow(expected_headers)

                csv_writer.writerow([patient_id, updated_image_filename, image_size, current_time, sex_val, uhid_val, age_val, wt_val, bmi_val, ht_val, history_dermatological_disease_val, history_spectacle_use_val, bp_val, pr_val, cd_val, ld_val, gbs_val, cancers_val, lung_val, liver_val, abdomen_val, breast_val, brain_val, diabetes_val, diabetes_duration_val, hypr_val, hypr_dr_val, dyslipedemia_val, dyslipedemia_dr_val, hypothyroid_val, hypothyroid_dr_val, hyperthyroid_val, hyperthyroid_dr_val, cardiac_disease_val, cardiac_disease_dr_val, respiratory_val, respiratory_dr_val, renal_val, renal_dr_val,chronic_liver_disease_val, ethanol_val,bleed_Bleeder_val, nash_val, hepatitis_b_val,encephalopathy_val,hepatitis_c_val, autoimmune_val, ascites_val,upper_gi_bleed_val, jaundice_val,hepatic_val,hcc_val,heamoglobin_val,creatinine_val,platelet_count_val, urea_val, fasting_blood_sugar_val, sodium_val, postprandial_blood_sugar_val, fibroscan_val, hba1c_val,endoscopy_val, bilirubin_val])

            label.configure(text="Image Captured and Saved!\nPress ENTER to capture more", text_color="green")
            camera_feed_label.pack()
            encrypt(key, updated_image_filename)
            insert_data_to_sql_database('localhost', 'root', 'Nikhil#1', 'test', pd.read_csv('captured_image_details.csv'))
        else:
            os.remove(updated_image_filename)  # Delete the image if not saved
            label.configure(text="Image Discarded", fg_color="red")
        photo = None
        mouse_pressed = False  # Declare mouse_pressed as a global variable
        captured_frame = None
        image_filename = None
        mouse_pressed = False
        confirmation = None
        _flag = True
        file_path = None
        image_copy = None
        frame = None
        ret = None
        current_time = None
        image_label.configure(image=None)
    else:
        messagebox.showerror("Error", "No image captured")
    
def update_camera_feed():
    global camera_feed_label

    ret, frame = camera_capture.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)

        # Get the dimensions of the frame
        height, width, channels = frame.shape

        # Calculate the coordinates for the center of the frame
        center_x = width // 2
        center_y = height // 2

        # Define the size of the green rectangle
        rect_width = 325
        rect_height = 470

        # Calculate the coordinates for the top-left and bottom-right corners of the rectangle
        rect_x1 = center_x - rect_width // 2
        rect_y1 = center_y - rect_height // 2
        rect_x2 = center_x + rect_width // 2
        rect_y2 = center_y + rect_height // 2

        # Draw a green rectangle on the frame
        cv2.rectangle(frame, (rect_x1, rect_y1), (rect_x2, rect_y2), (0, 255, 0), 2)

        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        camera_feed_label.config(image=photo)
        camera_feed_label.image = photo
        camera_feed_label.after(10, update_camera_feed)
    else:
        camera_feed_label.after(10, update_camera_feed)
        
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
flag_saved = False
photo = None
mouse_pressed = False  # Declare mouse_pressed as a global variable
captured_frame = None
image_filename = None
mouse_pressed = False
confirmation = None
_flag = True
file_path = None
image_copy = None
frame = None
ret = None 
current_time = None
entry_text = None
clear_flag = 0 

## part2 variables 

states = (('Yes', 'Y'), ('No', 'N'))
font_size = 10 
# history_dermatological_disease = tk.StringVar()
# # history_dermatological_disease_states = (('Yes', 'Y'), ('No', 'N'))
# history_spectacles = tk.StringVar()
# # history_spectacles_states = (('Yes', 'Y'), ('No', 'N'))
# blood_pressure = tk.StringVar()
# entry_blood_pressure = ""
# pulse_rate = tk.StringVar()
# entry_pulse_rate = ""
#     #family h/o
# cardiac_disease = tk.StringVar()
# # cardiac_disease_states = (('Yes', 'Y'), ('No', 'N'))
# liver_disease = tk.StringVar()
# # liver_disease_states = (('Yes', 'Y'), ('No', 'N'))  
# gall_bladder_stones = tk.StringVar()
# # gall_bladder_stones_states = (('Yes', 'Y'), ('No', 'N'))
# cancers = tk.StringVar()
# # cancers_states = (('Yes', 'Y'), ('No', 'N'))
# lung_disease = tk.StringVar()
# # lung_disease_states = (('Yes', 'Y'), ('No', 'N'))
# liver_disease = tk.StringVar()
# # liver_disease_states = (('Yes', 'Y'), ('No', 'N'))
# abdominal_disease = tk.StringVar()
# # abdominal_disease_states = (('Yes', 'Y'), ('No', 'N'))
# breast_disease = tk.StringVar()
# # breast_disease_states = (('Yes', 'Y'), ('No', 'N'))
# brain_disease = tk.StringVar()
# brain_disease_states = (('Yes', 'Y'), ('No', 'N'))
root.title("Image Capture")
root.minsize(800, 800)

frame_outside = ctk.CTkFrame(root, height=850, width=1600, bg_color="black",)
frame_outside.bind("<Configure>",  frame_outside.place(relx=0.5, rely=0.5, anchor='center'))
frame_patient_details = ctk.CTkFrame(root, height=230, width=1520, bg_color="black",fg_color="#d3d3d3",corner_radius=0)
frame_patient_details.bind("<Configure>",  frame_patient_details.place(relx=0.5, rely=0.5, anchor='center'))
frame_patient_details.place(x=0, y=275)


label = ctk.CTkLabel(root, text='''Press "Enter"/ Click capture to capture an image''', font=("Helvetica", 24),corner_radius=5,bg_color="black",fg_color="white",text_color="black",wraplength=600)
label.bind("<Configure>",  label.place(relx=0.5, rely=0.5, anchor='center'))
label.place( x=0 , y = -470)

label_patient_id  = ctk.CTkLabel(frame_outside, text="Patient ID", font=("Helvetica", 24),corner_radius=5,bg_color="black",fg_color="white",text_color="black",wraplength=600)
label_patient_id.bind("<Configure>",  label_patient_id.place(relx=0.5, rely=0.5, anchor='center'))
label_patient_id.place( x=0 , y = -250)
validate_length = root.register(limit_input_length)

entry_var = tk.StringVar()
entry = tk.Entry(frame_outside,textvariable=entry_var, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Helvetica", 18), bg="white", fg="black", width=15)
entry.bind("<Configure>",  entry.place(relx=0.5, rely=0.5, anchor='center'))
entry_var.trace_add("write", on_entry_change)
entry.place( x=0 , y = -200)

frame_camera = tk.Frame(root,height=485,width=645, background="black")
frame_camera.bind("<Configure>",  frame_camera.place(relx=0.5, rely=0.5, anchor='center'))
frame_camera.place(x=-440, y = -85)

camera_feed_label = tk.Label(frame_camera,height=470,width=640, background="black")
camera_feed_label.bind("<Configure>",  camera_feed_label.place(relx=0.5, rely=0.5, anchor='center'))


frame_captured_image = tk.Frame(root,height=485,width=645, background="black")
frame_captured_image.bind("<Configure>",  frame_captured_image.place(relx=0.5, rely=0.5, anchor='center'))
frame_captured_image.place(x=440, y = -85)

image_label = tk.Label(frame_captured_image, image=None)
# image_label.bind("<Configure>",  image_label.place(relx=0.5, rely=0.5, anchor='center'))
# if image_filename != None : 
    # show_captured_image()
# imagee = Image.open("captured_images/captured_image_2023-10-07 05-30-06.jpeg")
# photoo = ImageTk.PhotoImage(imagee)
# image_label.config(image=photoo)

###### Labels #######
sex = tk.StringVar()
entry_sex = ""
sexes = (('M', 'M'), ('F', 'F'))
sex_label = ttk.Label(frame_patient_details,text= "Sex :",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
sex_label.bind("<Configure>", sex_label.place(relx=0.5, rely=0.5, anchor='center'))
sex_label.place(x=-730, y=-102)
x = -720
y = -105
for options in sexes:
    r = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=sex
    )
    # print(sex)
    r.bind("<Configure>",  r.place(relx=0.5, rely=0.5, anchor='center'))
    r.place(x=x+50, y=y+5)
    x = x + 40
sex.trace_add("write",on_sex_change)

uhid_label = ttk.Label(frame_patient_details,text= "UHID: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
uhid_label.bind("<Configure>", uhid_label.place(relx=0.5, rely=0.5, anchor='center'))
uhid_label.place(x=-730, y=-75)
uhid = tk.StringVar()
entry_uhid = ""  
entry_box_uhid = tk.Entry(frame_patient_details,textvariable=uhid, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_uhid.bind("<Configure>",  entry_box_uhid.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_uhid.place(x=-650, y=-75)
uhid.trace_add("write",on_id_change)

age_label = ttk.Label(frame_patient_details,text= "Age: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
age_label.bind("<Configure>", age_label.place(relx=0.5, rely=0.5, anchor='center'))
age_label.place(x=-730, y=-45)
age = tk.StringVar()
entry_age = ""
entry_box_age = tk.Entry(frame_patient_details,textvariable=age, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_age.bind("<Configure>",  entry_box_age.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_age.place(x=-650, y=-45)
age.trace_add("write",on_age_change)

weight_label = ttk.Label(frame_patient_details,text= "Weight: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
weight_label.bind("<Configure>", weight_label.place(relx=0.5, rely=0.5, anchor='center'))
weight_label.place(x=-730, y=-15)
weight = tk.StringVar()
entry_weight = ""
entry_box_weight = tk.Entry(frame_patient_details,textvariable=weight, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_weight.bind("<Configure>",  entry_box_weight.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_weight.place(x=-650, y=-15)
weight.trace_add("write",on_weight_change)

bmi_label = ttk.Label(frame_patient_details,text= "BMI: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
bmi_label.bind("<Configure>", bmi_label.place(relx=0.5, rely=0.5, anchor='center'))
bmi_label.place(x=-730, y=15)
bmi = tk.StringVar()
entry_bmi = ""
entry_box_bmi = tk.Entry(frame_patient_details,textvariable=bmi, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_bmi.bind("<Configure>",  entry_box_bmi.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_bmi.place(x=-650, y=15)
bmi.trace_add("write",on_bmi_change)

height_label = ttk.Label(frame_patient_details,text= "Height: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
height_label.bind("<Configure>", height_label.place(relx=0.5, rely=0.5, anchor='center'))
height_label.place(x=-730, y=45)
height = tk.StringVar()
entry_height = ""
entry_box_height = tk.Entry(frame_patient_details,textvariable=height, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_height.bind("<Configure>",  entry_box_height.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_height.place(x=-650, y=45)
height.trace_add("write",on_height_change)

history_dermatological_disease_label = ttk.Label(frame_patient_details,text= "History of \nDermatolog-\nical Disease: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
history_dermatological_disease_label.bind("<Configure>", history_dermatological_disease_label.place(relx=0.5, rely=0.5, anchor='center'))
history_dermatological_disease_label.place(x=-720, y=90)
history_dermatological_disease = tk.StringVar()
entry_history_dermatological_disease = ""
x1 = -710
y1 = 75
for options in states:
    r1 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=history_dermatological_disease
    )
    # print(history_dermatological_disease)
    r1.bind("<Configure>",  r1.place(relx=0.5, rely=0.5, anchor='center'))
    r1.place(x=x1+50, y=y1+5)
    x1 = x1 + 50
history_dermatological_disease.trace_add("write",on_history_dermatological_disease_change)

history_spectacle_use_label = ttk.Label(frame_patient_details,text= "History of \nSpectacle Use: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
history_spectacle_use_label.bind("<Configure>", history_spectacle_use_label.place(relx=0.5, rely=0.5, anchor='center'))
history_spectacle_use_label.place(x=-510, y=-90)
history_spectacles = tk.StringVar()
entry_history_spectacles = ""
x2 = -470
y2 = -100
for options in states:
    r2 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=history_spectacles
    )
    # print(history_spectacles)
    r2.bind("<Configure>",  r2.place(relx=0.5, rely=0.5, anchor='center'))
    r2.place(x=x2+50, y=y2+5)
    x2 = x2 + 50
history_spectacles.trace_add("write",on_history_spectacles_change)

blood_pressure_label = ttk.Label(frame_patient_details,text= "Blood Pressure: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
blood_pressure_label.bind("<Configure>", blood_pressure_label.place(relx=0.5, rely=0.5, anchor='center'))
blood_pressure_label.place(x=-510, y=-60)
blood_pressure = tk.StringVar()
entry_blood_pressure = ""
entry_box_blood_pressure = tk.Entry(frame_patient_details,textvariable=blood_pressure, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_blood_pressure.bind("<Configure>",  entry_box_blood_pressure.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_blood_pressure.place(x=-400, y=-60)
blood_pressure.trace_add("write",on_blood_pressure_change)

pulse_rate_label = ttk.Label(frame_patient_details,text= "Pulse Rate: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
pulse_rate_label.bind("<Configure>", pulse_rate_label.place(relx=0.5, rely=0.5, anchor='center'))
pulse_rate_label.place(x=-510, y=-30)
pulse_rate = tk.StringVar()
entry_pulse_rate = ""
entry_box_pulse_rate = tk.Entry(frame_patient_details,textvariable=pulse_rate, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_pulse_rate.bind("<Configure>",  entry_box_pulse_rate.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_pulse_rate.place(x=-400, y=-30)
pulse_rate.trace_add("write",on_pulse_rate_change)

cardiac_disease_label = ttk.Label(frame_patient_details,text= "Cardiac Disease: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
cardiac_disease_label.bind("<Configure>", cardiac_disease_label.place(relx=0.5, rely=0.5, anchor='center'))
cardiac_disease_label.place(x=-510, y=0)
cardiac_disease = tk.StringVar()
entry_cardiac_disease = ""
x3 = -470
y3 = -5
for options in states:
    r3 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=cardiac_disease
    )
    # print(cardiac_disease)
    r3.bind("<Configure>",  r3.place(relx=0.5, rely=0.5, anchor='center'))
    r3.place(x=x3+50, y=y3+5)
    x3 = x3 + 50
cardiac_disease.trace_add("write",on_cardiac_disease_change)

liver_disease_label = ttk.Label(frame_patient_details,text= "Liver Disease: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
liver_disease_label.bind("<Configure>", liver_disease_label.place(relx=0.5, rely=0.5, anchor='center'))
liver_disease_label.place(x=-510, y=30)
liver_disease = tk.StringVar()
entry_liver_disease = ""
x4 = -470
y4 = 25
for options in states:
    r4 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=liver_disease
    )
    # print(liver_disease)
    r4.bind("<Configure>",  r4.place(relx=0.5, rely=0.5, anchor='center'))
    r4.place(x=x4+50, y=y4+5)
    x4 = x4 + 50
liver_disease.trace_add("write",on_liver_disease_change)

gall_bladder_disease_label = ttk.Label(frame_patient_details,text= "Gall Bladder Stones: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
gall_bladder_disease_label.bind("<Configure>", gall_bladder_disease_label.place(relx=0.5, rely=0.5, anchor='center'))
gall_bladder_disease_label.place(x=-510, y=60)
gall_bladder_stones = tk.StringVar()
entry_gall_bladder_stones = ""
x5 = -470
y5 = 55
for options in states:
    r5 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=gall_bladder_stones
    )
    # print(gall_bladder_stones)
    r5.bind("<Configure>",  r5.place(relx=0.5, rely=0.5, anchor='center'))
    r5.place(x=x5+50, y=y5+5)
    x5 = x5 + 50
gall_bladder_stones.trace_add("write",on_gall_bladder_stones_change)

cancers_label = ttk.Label(frame_patient_details,text= "Cancers: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
cancers_label.bind("<Configure>", cancers_label.place(relx=0.5, rely=0.5, anchor='center'))
cancers_label.place(x=-510, y=90)
cancers = tk.StringVar()
entry_cancers = ""
x6 = -470
y6 = 85
for options in states:
    r6 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=cancers
    )
    # print(cancers)
    r6.bind("<Configure>",  r6.place(relx=0.5, rely=0.5, anchor='center'))
    r6.place(x=x6+50, y=y6+5)
    x6 = x6 + 50
cancers.trace_add("write",on_cancers_change)

lung_label = ttk.Label(frame_patient_details,text= "Lung: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
lung_label.bind("<Configure>", lung_label.place(relx=0.5, rely=0.5, anchor='center'))
lung_label.place(x=-300, y=-106)
lung = tk.StringVar()
entry_lung = ""
x7 = -290
y7 = -108
for options in states:
    r7 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=lung
    )
    # print(lung)
    r7.bind("<Configure>",  r7.place(relx=0.5, rely=0.5, anchor='center'))
    r7.place(x=x7+50, y=y7+5)
    x7 = x7 + 50
lung.trace_add("write",on_lung_change)

liver_label = ttk.Label(frame_patient_details,text= "Liver: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
liver_label.bind("<Configure>", liver_label.place(relx=0.5, rely=0.5, anchor='center'))
liver_label.place(x=-300, y=-82)
liver = tk.StringVar()
entry_liver = ""
x8 = -290
y8 = -85
for options in states:
    r8 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=liver
    )
    # print(liver)
    r8.bind("<Configure>",  r8.place(relx=0.5, rely=0.5, anchor='center'))
    r8.place(x=x8+50, y=y8+5)
    x8 = x8 + 50
liver.trace_add("write",on_liver_change)

abdomen_label = ttk.Label(frame_patient_details,text= "Abdomen: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
abdomen_label.bind("<Configure>", abdomen_label.place(relx=0.5, rely=0.5, anchor='center'))
abdomen_label.place(x=-300, y=-59)
abdominal = tk.StringVar()
entry_abdominal = ""
x9 = -290
y9 = -61
for options in states:
    r9 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=abdominal
    )
    # print(abdominal)
    r9.bind("<Configure>",  r9.place(relx=0.5, rely=0.5, anchor='center'))
    r9.place(x=x9+50, y=y9+5)
    x9 = x9 + 50
abdominal.trace_add("write",on_abdominal_change)

breast_label = ttk.Label(frame_patient_details,text= "Breast: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
breast_label.bind("<Configure>", breast_label.place(relx=0.5, rely=0.5, anchor='center'))
breast_label.place(x=-300, y=-35)
breast = tk.StringVar()
entry_breast = ""
x10 = -290
y10 = -37
for options in states:
    r10 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=breast
    )
    # print(breast)
    r10.bind("<Configure>",  r10.place(relx=0.5, rely=0.5, anchor='center'))
    r10.place(x=x10+50, y=y10+5)
    x10 = x10 + 50
breast.trace_add("write",on_breast_change)

brain_label = ttk.Label(frame_patient_details,text= "Brain: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
brain_label.bind("<Configure>", brain_label.place(relx=0.5, rely=0.5, anchor='center'))
brain_label.place(x=-300, y=-13)
brain = tk.StringVar()
entry_brain = ""
x11 = -290
y11 = -13
for options in states:
    r11 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=brain
    )
    # print(brain)
    r11.bind("<Configure>",  r11.place(relx=0.5, rely=0.5, anchor='center'))
    r11.place(x=x11+50, y=y11+5)
    x11 = x11 + 50
brain.trace_add("write",on_brain_change)

label_patient_illness = ctk.CTkLabel(frame_patient_details, text='''Illness''', font=("Helvetica", 12, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_patient_illness.bind("<Configure>",  label_patient_illness.place(relx=0.5, rely=0.5, anchor='center'))
label_patient_illness.place( x=-110 , y = -103)

label_yes_no = ctk.CTkLabel(frame_patient_details, text='''Yes/No''', font=("Helvetica", 12, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_yes_no.bind("<Configure>",  label_yes_no.place(relx=0.5, rely=0.5, anchor='center'))
label_yes_no.place( x=0 , y = -103)

label_months = ctk.CTkLabel(frame_patient_details, text='''Duration (Months)''', font=("Helvetica", 12, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_months.bind("<Configure>",  label_months.place(relx=0.5, rely=0.5, anchor='center'))
label_months.place( x=100 , y = -103)

label_diabetes = ctk.CTkLabel(frame_patient_details, text='''Diabetes''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_diabetes.bind("<Configure>",  label_diabetes.place(relx=0.5, rely=0.5, anchor='center'))
label_diabetes.place( x=-110 , y = -80)
diabetes = tk.StringVar()
entry_diabetes = ""
x12 = -65
y12 = -85
for options in states:
    r12 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=diabetes
    )
    # print(diabetes)
    r12.bind("<Configure>",  r12.place(relx=0.5, rely=0.5, anchor='center'))
    r12.place(x=x12+50, y=y12+5)
    x12 = x12 + 50
diabetes.trace_add("write",on_diabetes_change)
diabetes_duration = tk.StringVar()
entry_diabetes_duration = ""
entry_box_diabetes = tk.Entry(frame_patient_details,textvariable=diabetes_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_diabetes.bind("<Configure>",  entry_box_diabetes.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_diabetes.place(x=100, y=-80)
diabetes_duration.trace_add("write",on_diabetes_duration_change)    

label_hypertention = ctk.CTkLabel(frame_patient_details, text='''Hypertention''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_hypertention.bind("<Configure>",  label_hypertention.place(relx=0.5, rely=0.5, anchor='center'))
label_hypertention.place( x=-110 , y = -55)
hypertention = tk.StringVar()
entry_hypertention = ""
x13 = -65
y13 = -60
for options in states:
    r13 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hypertention
    )
    # print(hypertention)
    r13.bind("<Configure>",  r13.place(relx=0.5, rely=0.5, anchor='center'))
    r13.place(x=x13+50, y=y13+5)
    x13 = x13 + 50
hypertention.trace_add("write",on_hypertention_change)
hypertention_duration = tk.StringVar()
entry_hypertention_duration = ""
entry_box_hypertention = tk.Entry(frame_patient_details,textvariable=hypertention_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_hypertention.bind("<Configure>",  entry_box_hypertention.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_hypertention.place(x=100, y=-55)
hypertention_duration.trace_add("write",on_hypertention_duration_change)

label_dyslipedemia = ctk.CTkLabel(frame_patient_details, text='''Dyslipedemia\n(Chol>200/T.G>200)''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_dyslipedemia.bind("<Configure>",  label_dyslipedemia.place(relx=0.5, rely=0.5, anchor='center'))
label_dyslipedemia.place( x=-110 , y = -30)
dyslipedemia = tk.StringVar()
entry_dyslipedemia = ""
x14 = -65
y14 = -35
for options in states:
    r14 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=dyslipedemia
    )
    # print(dyslipedemia)
    r14.bind("<Configure>",  r14.place(relx=0.5, rely=0.5, anchor='center'))
    r14.place(x=x14+50, y=y14+5)
    x14 = x14 + 50
dyslipedemia.trace_add("write",on_dyslipedemia_change)
dyslipedemia_duration = tk.StringVar()
entry_dyslipedemia_duration = ""
entry_box_dyslipedemia = tk.Entry(frame_patient_details,textvariable=dyslipedemia_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_dyslipedemia.bind("<Configure>",  entry_box_dyslipedemia.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_dyslipedemia.place(x=100, y=-30)
dyslipedemia_duration.trace_add("write",on_dyslipedemia_duration_change)

label_hypothyriod = ctk.CTkLabel(frame_patient_details, text='''Hypothyriod''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_hypothyriod.bind("<Configure>",  label_hypothyriod.place(relx=0.5, rely=0.5, anchor='center'))
label_hypothyriod.place( x=-110 , y = -5)
hypothyroid = tk.StringVar()
entry_hypothyroid = ""
x15 = -65
y15 = -10
for options in states:
    r15 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hypothyroid
    )
    # print(hypothyroid)
    r15.bind("<Configure>",  r15.place(relx=0.5, rely=0.5, anchor='center'))
    r15.place(x=x15+50, y=y15+5)
    x15 = x15 + 50
hypothyroid.trace_add("write",on_hypothyroid_change)
hypothyroid_duration = tk.StringVar()
entry_hypothyroid_duration = ""
entry_box_hypothyroid = tk.Entry(frame_patient_details,textvariable=hypothyroid_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_hypothyroid.bind("<Configure>",  entry_box_hypothyroid.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_hypothyroid.place(x=100, y=-5)
hypothyroid_duration.trace_add("write",on_hypothyroid_duration_change)

label_hyperthyriod = ctk.CTkLabel(frame_patient_details, text='''Hyperthyriod''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_hyperthyriod.bind("<Configure>",  label_hyperthyriod.place(relx=0.5, rely=0.5, anchor='center'))
label_hyperthyriod.place( x=-110 , y = 20)
hyperthyroid = tk.StringVar()
entry_hyperthyroid = ""
x16 = -65
y16 = 15
for options in states:
    r16 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hyperthyroid
    )
    # print(hyperthyroid)
    r16.bind("<Configure>",  r16.place(relx=0.5, rely=0.5, anchor='center'))
    r16.place(x=x16+50, y=y16+5)
    x16 = x16 + 50
hyperthyroid.trace_add("write",on_hyperthyroid_change)
hyperthyroid_duration = tk.StringVar()
entry_hyperthyroid_duration = ""
entry_box_hyperthyroid = tk.Entry(frame_patient_details,textvariable=hyperthyroid_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_hyperthyroid.bind("<Configure>",  entry_box_hyperthyroid.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_hyperthyroid.place(x=100, y=20)
hyperthyroid_duration.trace_add("write",on_hyperthyroid_duration_change)

label_cardiac_disease = ctk.CTkLabel(frame_patient_details, text='''Cardiac Disease''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_cardiac_disease.bind("<Configure>",  label_cardiac_disease.place(relx=0.5, rely=0.5, anchor='center'))
label_cardiac_disease.place( x=-110 , y = 45)
cardiac = tk.StringVar()
entry_cardiac = ""
x17 = -65
y17 = 40
for options in states:
    r17 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=cardiac
    )
    # print(cardiac)
    r17.bind("<Configure>",  r17.place(relx=0.5, rely=0.5, anchor='center'))
    r17.place(x=x17+50, y=y17+5)
    x17 = x17 + 50
cardiac.trace_add("write",on_cardiac_change)
cardiac_duration = tk.StringVar()
entry_cardiac_duration = ""
entry_box_cardiac = tk.Entry(frame_patient_details,textvariable=cardiac_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_cardiac.bind("<Configure>",  entry_box_cardiac.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_cardiac.place(x=100, y=45)
cardiac_duration.trace_add("write",on_cardiac_duration_change)

label_respiratory_disease = ctk.CTkLabel(frame_patient_details, text='''Respiratory Disease''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)
label_respiratory_disease.bind("<Configure>",  label_respiratory_disease.place(relx=0.5, rely=0.5, anchor='center'))
label_respiratory_disease.place( x=-110 , y = 70)
respiratory = tk.StringVar()
entry_respiratory = ""
x18 = -65
y18 = 65
for options in states:
    r18 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=respiratory
    )
    # print(respiratory)
    r18.bind("<Configure>",  r18.place(relx=0.5, rely=0.5, anchor='center'))
    r18.place(x=x18+50, y=y18+5)
    x18 = x18 + 50
respiratory.trace_add("write",on_respiratory_change)
respiratory_duration = tk.StringVar()
entry_respiratory_duration = ""
entry_box_respiratory = tk.Entry(frame_patient_details,textvariable=respiratory_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_respiratory.bind("<Configure>",  entry_box_respiratory.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_respiratory.place(x=100, y=70)
respiratory_duration.trace_add("write",on_respiratory_duration_change)

label_renal_disease = ctk.CTkLabel(frame_patient_details, text='''Renal Disease''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)    
label_renal_disease.bind("<Configure>",  label_renal_disease.place(relx=0.5, rely=0.5, anchor='center'))
label_renal_disease.place( x=-110 , y = 95)
renal = tk.StringVar()
entry_renal = ""
x19 = -65
y19 = 90
for options in states:
    r19 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=renal
    )
    # print(renal)
    r19.bind("<Configure>",  r19.place(relx=0.5, rely=0.5, anchor='center'))
    r19.place(x=x19+50, y=y19+5)
    x19 = x19 + 50
renal.trace_add("write",on_renal_change)
renal_duration = tk.StringVar()
entry_renal_duration = ""
entry_box_renal = tk.Entry(frame_patient_details,textvariable=renal_duration, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10,state='disabled')
entry_box_renal.bind("<Configure>",  entry_box_renal.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_renal.place(x=100, y=95)
renal_duration.trace_add("write",on_renal_duration_change)


# pulse_rate_label = ttk.Label(frame_patient_details,text= "Pulse Rate: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
# pulse_rate_label.bind("<Configure>", pulse_rate_label.place(relx=0.5, rely=0.5, anchor='center'))
# pulse_rate_label.place(x=-510, y=-30)
# pulse_rate = tk.StringVar()
# entry_pulse_rate = ""
# entry_box_pulse_rate = tk.Entry(frame_patient_details,textvariable=pulse_rate, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
# entry_box_pulse_rate.bind("<Configure>",  entry_box_pulse_rate.place(relx=0.5, rely=0.5, anchor='center'))
# entry_box_pulse_rate.place(x=-400, y=-30)
# pulse_rate.trace_add("write",on_pulse_rate_change)


heamoglobin_label = ttk.Label(frame_patient_details,text= "Heamoglobin: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
heamoglobin_label.bind("<Configure>", heamoglobin_label.place(relx=0.5, rely=0.5, anchor='center'))
heamoglobin_label.place(x=219, y=-90)
heamoglobin = tk.StringVar()
entry_heamoglobin = ""
entry_box_heamoglobin = tk.Entry(frame_patient_details,textvariable=heamoglobin, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_heamoglobin.bind("<Configure>",  entry_box_heamoglobin.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_heamoglobin.place(x=319, y=-90)
heamoglobin.trace_add("write",on_heamoglobin_change)

creatinine_label = ttk.Label(frame_patient_details,text= "Creatinine: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
creatinine_label.bind("<Configure>", creatinine_label.place(relx=0.5, rely=0.5, anchor='center'))
creatinine_label.place(x=419, y=-90)
creatinine = tk.StringVar()
entry_creatinine = ""
entry_box_creatinine = tk.Entry(frame_patient_details,textvariable=creatinine, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_creatinine.bind("<Configure>",  entry_box_creatinine.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_creatinine.place(x=519, y=-90)
creatinine.trace_add("write",on_creatinine_change)

platelet_count_label = ttk.Label(frame_patient_details,text= "Platelet Count: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
platelet_count_label.bind("<Configure>", platelet_count_label.place(relx=0.5, rely=0.5, anchor='center'))
platelet_count_label.place(x=219, y=-65)
platelet_count = tk.StringVar()
entry_platelet_count = ""
entry_box_platelet_count = tk.Entry(frame_patient_details,textvariable=platelet_count, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_platelet_count.bind("<Configure>",  entry_box_platelet_count.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_platelet_count.place(x=319, y=-65)
platelet_count.trace_add("write",on_platelet_count_change)

urea_label = ttk.Label(frame_patient_details,text= "Urea(mg/dl): ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
urea_label.bind("<Configure>", urea_label.place(relx=0.5, rely=0.5, anchor='center'))
urea_label.place(x=419, y=-65)
urea = tk.StringVar()
entry_urea = ""
entry_box_urea = tk.Entry(frame_patient_details,textvariable=urea, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_urea.bind("<Configure>",  entry_box_urea.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_urea.place(x=519, y=-65)
urea.trace_add("write",on_urea_change)

fasting_blood_sugar_label = ttk.Label(frame_patient_details,text= "FBS(mg/dl): ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
fasting_blood_sugar_label.bind("<Configure>", fasting_blood_sugar_label.place(relx=0.5, rely=0.5, anchor='center'))
fasting_blood_sugar_label.place(x=219, y=-40)
fasting_blood_sugar = tk.StringVar()
entry_fasting_blood_sugar = ""
entry_box_fasting_blood_sugar = tk.Entry(frame_patient_details,textvariable=fasting_blood_sugar, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_fasting_blood_sugar.bind("<Configure>",  entry_box_fasting_blood_sugar.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_fasting_blood_sugar.place(x=319, y=-40)
fasting_blood_sugar.trace_add("write",on_fasting_blood_sugar_change)

sodium_label = ttk.Label(frame_patient_details,text= "Sodium: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
sodium_label.bind("<Configure>", sodium_label.place(relx=0.5, rely=0.5, anchor='center'))
sodium_label.place(x=419, y=-40)
sodium = tk.StringVar()
entry_sodium = ""
entry_box_sodium = tk.Entry(frame_patient_details,textvariable=sodium, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_sodium.bind("<Configure>",  entry_box_sodium.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_sodium.place(x=519, y=-40)
sodium.trace_add("write",on_sodium_change)

on_postprandial_blood_sugar_label = ttk.Label(frame_patient_details,text= "PPG: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
on_postprandial_blood_sugar_label.bind("<Configure>", on_postprandial_blood_sugar_label.place(relx=0.5, rely=0.5, anchor='center'))
on_postprandial_blood_sugar_label.place(x=219, y=-15)
postprandial_blood_sugar = tk.StringVar()
entry_postprandial_blood_sugar = ""
entry_box_on_postprandial_blood_sugar = tk.Entry(frame_patient_details,textvariable=postprandial_blood_sugar, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_on_postprandial_blood_sugar.bind("<Configure>",  entry_box_on_postprandial_blood_sugar.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_on_postprandial_blood_sugar.place(x=319, y=-15)
postprandial_blood_sugar.trace_add("write",on_postprandial_blood_sugar_change)

fibroscan_label = ttk.Label(frame_patient_details,text= "Fibroscan: ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
fibroscan_label.bind("<Configure>", fibroscan_label.place(relx=0.5, rely=0.5, anchor='center'))
fibroscan_label.place(x=419, y=-15)
fibroscan = tk.StringVar()
entry_fibroscan = ""
entry_box_fibroscan = tk.Entry(frame_patient_details,textvariable=fibroscan, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_fibroscan.bind("<Configure>",  entry_box_fibroscan.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_fibroscan.place(x=519, y=-15)
fibroscan.trace_add("write",on_fibroscan_change)

# label_renal_disease = ctk.CTkLabel(frame_patient_details, text='''Renal Disease''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black",wraplength=600,)    
# label_renal_disease.bind("<Configure>",  label_renal_disease.place(relx=0.5, rely=0.5, anchor='center'))
# label_renal_disease.place( x=-110 , y = 95)
# renal = tk.StringVar()
# entry_renal = ""
# x19 = -65
# y19 = 90
# for options in states:
#     r19 = ttk.Radiobutton(
#         frame_patient_details,
#         text=options[0],
#         value=options[1],
#         variable=renal
#     )
    # print(renal)
#     r19.bind("<Configure>",  r19.place(relx=0.5, rely=0.5, anchor='center'))
#     r19.place(x=x19+50, y=y19+5)
#     x19 = x19 + 50
# renal.trace_add("write",on_renal_change)

label_chronic_liver_disease = ctk.CTkLabel(frame_patient_details, text='''Chronic Liver:\nDisease(CLD)''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_chronic_liver_disease.bind("<Configure>",  label_chronic_liver_disease.place(relx=0.5, rely=0.5, anchor='center'))
label_chronic_liver_disease.place( x=219 , y = 18)
chronic_liver_disease = tk.StringVar()
entry_chronic_liver_disease = ""
x20 = 249
y20 = 15
for options in states:
    r20 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=chronic_liver_disease
    )
    # print(chronic_liver_disease)
    r20.bind("<Configure>",  r20.place(relx=0.5, rely=0.5, anchor='center'))
    r20.place(x=x20+50, y=y20+5)
    x20 = x20 + 50
chronic_liver_disease.trace_add("write",on_chronic_liver_disease_change)

label_ethanol = ctk.CTkLabel(frame_patient_details, text='''Ethanol:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_ethanol.bind("<Configure>",  label_ethanol.place(relx=0.5, rely=0.5, anchor='center'))
label_ethanol.place( x=219 , y = 43)
ethanol = tk.StringVar()
entry_ethanol = ""
x21 = 249
y21 = 40
for options in states:
    r21 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=ethanol
    )
    # print(ethanol)
    r21.bind("<Configure>",  r21.place(relx=0.5, rely=0.5, anchor='center'))
    r21.place(x=x21+50, y=y21+5)
    x21 = x21 + 50
ethanol.trace_add("write",on_ethanol_change)

label_bleed = ctk.CTkLabel(frame_patient_details, text='''Bleed:\n(Bleeder)''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_bleed.bind("<Configure>",  label_bleed.place(relx=0.5, rely=0.5, anchor='center'))
label_bleed.place( x=219 , y = 68)
bleed = tk.StringVar()
entry_bleed = ""
x22 = 249
y22 = 65
for options in states:
    r22 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=bleed
    )
    # print(bleed)
    r22.bind("<Configure>",  r22.place(relx=0.5, rely=0.5, anchor='center'))
    r22.place(x=x22+50, y=y22+5)
    x22 = x22 + 50
bleed.trace_add("write",on_bleed_change)

label_nash = ctk.CTkLabel(frame_patient_details, text='''NASH:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_nash.bind("<Configure>",  label_nash.place(relx=0.5, rely=0.5, anchor='center'))
label_nash.place( x=219 , y = 93)
nash = tk.StringVar()
entry_nash = ""
x23 = 249
y23 = 90
for options in states:
    r23 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=nash
    )
    # print(nash)
    r23.bind("<Configure>",  r23.place(relx=0.5, rely=0.5, anchor='center'))
    r23.place(x=x23+50, y=y23+5)
    x23 = x23 + 50
nash.trace_add("write",on_nash_change)

label_hepatitis_b = ctk.CTkLabel(frame_patient_details, text='''Hepatitis B:\n(HBV)''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_hepatitis_b.bind("<Configure>",  label_hepatitis_b.place(relx=0.5, rely=0.5, anchor='center'))
label_hepatitis_b.place( x=419 , y = 18)
hepatitis_b = tk.StringVar()
entry_hepatitis_b = ""
x24 = 450
y24 = 15
for options in states:
    r24 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hepatitis_b
    )
    # print(hepatitis_b)
    r24.bind("<Configure>",  r24.place(relx=0.5, rely=0.5, anchor='center'))
    r24.place(x=x24+50, y=y24+5)
    x24 = x24 + 50
hepatitis_b.trace_add("write",on_hepatitis_b_change)

label_encephalopathy = ctk.CTkLabel(frame_patient_details, text='''Encephalopathy:\n(HE)''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_encephalopathy.bind("<Configure>",  label_encephalopathy.place(relx=0.5, rely=0.5, anchor='center'))
label_encephalopathy.place( x=419 , y = 43)
encephalopathy = tk.StringVar()
entry_encephalopathy = ""
x25 = 450
y25 = 40
for options in states:
    r25 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=encephalopathy
    )
    # print(encephalopathy)
    r25.bind("<Configure>",  r25.place(relx=0.5, rely=0.5, anchor='center'))
    r25.place(x=x25+50, y=y25+5)
    x25 = x25 + 50
encephalopathy.trace_add("write",on_encephalopathy_change)

label_hepatitis_c = ctk.CTkLabel(frame_patient_details, text='''Hepatitis C:\n(HCV)''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_hepatitis_c.bind("<Configure>",  label_hepatitis_c.place(relx=0.5, rely=0.5, anchor='center'))
label_hepatitis_c.place( x=419 , y = 68)
hepatitis_c = tk.StringVar()
entry_hepatitis_c = ""
x26 = 450
y26 = 65
for options in states:
    r26 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hepatitis_c
    )
    # print(hepatitis_c)
    r26.bind("<Configure>",  r26.place(relx=0.5, rely=0.5, anchor='center'))
    r26.place(x=x26+50, y=y26+5)
    x26 = x26 + 50
hepatitis_c.trace_add("write",on_hepatitis_c_change)

label_autoimmune = ctk.CTkLabel(frame_patient_details, text='''Autoimmune:\n(AIH)''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_autoimmune.bind("<Configure>",  label_autoimmune.place(relx=0.5, rely=0.5, anchor='center'))
label_autoimmune.place( x=419 , y = 93)
autoimmune = tk.StringVar()
entry_autoimmune = ""
x27 = 450
y27 = 90
for options in states:
    r27 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=autoimmune
    )
    # print(autoimmune)
    r27.bind("<Configure>",  r27.place(relx=0.5, rely=0.5, anchor='center'))
    r27.place(x=x27+50, y=y27+5)
    x27 = x27 + 50
autoimmune.trace_add("write",on_autoimmune_change)

label_ascites = ctk.CTkLabel(frame_patient_details, text='''Ascites:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_ascites.bind("<Configure>",  label_ascites.place(relx=0.5, rely=0.5, anchor='center'))
label_ascites.place( x=-300 , y = 12)
ascites = tk.StringVar()
entry_ascites = ""
x28 = -290
y28 = 10
for options in states:
    r28 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=ascites
    )
    # print(ascites)
    r28.bind("<Configure>",  r28.place(relx=0.5, rely=0.5, anchor='center'))
    r28.place(x=x28+50, y=y28+5)
    x28 = x28 + 50
ascites.trace_add("write",on_ascites_change)

label_upper_gi_bleed = ctk.CTkLabel(frame_patient_details, text='''Upper GI:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3",text_color="black")
label_upper_gi_bleed.bind("<Configure>",  label_upper_gi_bleed.place(relx=0.5, rely=0.5, anchor='center'))
label_upper_gi_bleed.place( x=-300 , y = 37)
upper_gi_bleed = tk.StringVar()
entry_upper_gi_bleed = ""
x29 = -290
y29 = 33
for options in states:
    r29 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=upper_gi_bleed
    )
    # print(upper_gi_bleed)
    r29.bind("<Configure>",  r29.place(relx=0.5, rely=0.5, anchor='center'))
    r29.place(x=x29+50, y=y29+5)
    x29 = x29 + 50
upper_gi_bleed.trace_add("write",on_upper_gi_change)

label_jaundice = ctk.CTkLabel(frame_patient_details, text='''Jaundice:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3", text_color="black")
label_jaundice.bind("<Configure>",  label_jaundice.place(relx=0.5, rely=0.5, anchor='center'))
label_jaundice.place( x=-300 , y = 62)
jaundice = tk.StringVar()
entry_jaundice = ""
x30 = -290
y30 = 56
for options in states:
    r30 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=jaundice
    )
    # print(jaundice)
    r30.bind("<Configure>",  r30.place(relx=0.5, rely=0.5, anchor='center'))
    r30.place(x=x30+50, y=y30+5)
    x30 = x30 + 50
jaundice.trace_add("write",on_jaundice_change)

label_hepatic = ctk.CTkLabel(frame_patient_details, text='''Hepatic:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3", text_color="black")
label_hepatic.bind("<Configure>",  label_hepatic.place(relx=0.5, rely=0.5, anchor='center'))
label_hepatic.place( x=-300 , y = 87)
hepatic = tk.StringVar()
entry_hepatic = ""
x31 = -290
y31 = 81
for options in states:
    r31 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hepatic
    )
    # print(hepatic)
    r31.bind("<Configure>",  r31.place(relx=0.5, rely=0.5, anchor='center'))
    r31.place(x=x31+50, y=y31+5)
    x31 = x31 + 50
hepatic.trace_add("write",on_hepatic_change)

label_hcc = ctk.CTkLabel(frame_patient_details, text='''HCC:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3", text_color="black")
label_hcc.bind("<Configure>",  label_hcc.place(relx=0.5, rely=0.5, anchor='center'))
label_hcc.place( x=595 , y = -90)
hcc = tk.StringVar()
entry_hcc = ""
x32 = 625
y32 = -90
for options in states:
    r32 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hcc
    )
    # print(hcc)
    r32.bind("<Configure>",  r32.place(relx=0.5, rely=0.5, anchor='center'))
    r32.place(x=x32+50, y=y32+5)
    x32 = x32 + 50
hcc.trace_add("write",on_hcc_change)

states_hba1c = (('Varices', 'Varices'), ('PHG', 'PHG'))
label_hba1c = ctk.CTkLabel(frame_patient_details, text='''HbA1c:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3", text_color="black")
label_hba1c.bind("<Configure>",  label_hba1c.place(relx=0.5, rely=0.5, anchor='center'))
label_hba1c.place( x=595 , y = -65)
hba1c = tk.StringVar()
entry_hba1c = ""
x33 = 625
y33 = -65
for options in states_hba1c:
    r33 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=hba1c
    )
    # print(hba1c)
    r33.bind("<Configure>",  r33.place(relx=0.5, rely=0.5, anchor='center'))
    r33.place(x=x33+50, y=y33+5)
    x33 = x33 + 50
hba1c.trace_add("write",on_hba1c_change)

states_endoscopy = (('G1', 'Grade 1'), ('G2', 'Grade 2'), ('G3', 'Grade 3'))

label_endoscopy = ctk.CTkLabel(frame_patient_details, text='''Endoscopy:''', font=("Helvetica", 11, 'bold'),corner_radius=5,bg_color="#d3d3d3",fg_color="#d3d3d3", text_color="black")
label_endoscopy.bind("<Configure>",  label_endoscopy.place(relx=0.5, rely=0.5, anchor='center'))
label_endoscopy.place( x=595 , y = -40)
endoscopy = tk.StringVar()
entry_endoscopy = ""
x34 = 610
y34 = -40
for options in states_endoscopy:
    r34 = ttk.Radiobutton(
        frame_patient_details,
        text=options[0],
        value=options[1],
        variable=endoscopy
    )
    # print(endoscopy)
    r34.bind("<Configure>",  r34.place(relx=0.5, rely=0.5, anchor='center'))
    r34.place(x=x34+50, y=y34+5)
    x34 = x34 + 35
endoscopy.trace_add("write",on_endoscopy_change)


label_bilirubin = ttk.Label(frame_patient_details,text= "Bilirubin\n(mg/dl): ",background="#d3d3d3",font=("Calibri Light", 10,'bold'))
label_bilirubin.bind("<Configure>", label_bilirubin.place(relx=0.5, rely=0.5, anchor='center'))
label_bilirubin.place(x=600, y=-5)
bilirubin = tk.StringVar()
entry_bilirubin = ""
# entry_bilirubin = tk.StringVar()
entry_box_bilirubin = tk.Entry(frame_patient_details,textvariable=bilirubin, validate="key", validatecommand=(validate_length, '%P'), border=1, font=("Calibri Light", 10), bg="white", fg="black", width=10)
entry_box_bilirubin.bind("<Configure>",  entry_box_bilirubin.place(relx=0.5, rely=0.5, anchor='center'))
entry_box_bilirubin.place(x=675, y=-5)
bilirubin.trace_add("write",on_bilirubin_change)

capture_button = bttn(frame_outside, 0, -100, "Capture", '#808080', 'white','white', lambda: show_captured_image(None) ,'normal',"" ,2,20,("Calibri Light", 11,'bold'))
capture_button.bind("<Configure>",  capture_button.place(relx=0.5, rely=0.5, anchor='center'))

crop_button = bttn(frame_outside, 0, -50, "Crop", '#808080', 'white','white', lambda: crop_image(image_filename, image_filename) ,'normal',"" ,2,20,("Calibri Light", 11,'bold'))
crop_button.bind("<Configure>",  crop_button.place(relx=0.5, rely=0.5, anchor='center'))

undo_button = bttn(frame_outside, 0, 0, "Undo", '#808080', 'white','white', lambda: undo() ,'normal',"" ,2,20,("Calibri Light", 11,'bold'))
undo_button.bind("<Configure>",  undo_button.place(relx=0.5, rely=0.5, anchor='center'))

save_button = bttn(frame_outside, 0, 50, "Save", '#808080', 'white','white', lambda: save_photo() ,'normal',"" ,2,20,("Calibri Light", 11,'bold'))
save_button.bind("<Configure>",  save_button.place(relx=0.5, rely=0.5, anchor='center'))

clear_button = bttn(frame_outside, 0, 100, "Clear All", '#808080', 'white','white', lambda: clear_all() ,'normal',"" ,2,20,("Calibri Light", 11,'bold'))
clear_button.bind("<Configure>",  clear_button.place(relx=0.5, rely=0.5, anchor='center'))

# button_patient_id = bttn(frame_outside, 0, -150, "Enter", '#808080', 'white','white', lambda: get_id() ,'normal',"" ,2,20,("Calibri Light", 11,'bold'))
# button_patient_id.bind("<Configure>",  button_patient_id.place(relx=0.5, rely=0.5, anchor='center'))
camera_capture = cv2.VideoCapture(0)
frame_camera.after(10, update_camera_feed)  # Start the camera feed update loop
root.bind('<Return>', show_captured_image)
root.mainloop()