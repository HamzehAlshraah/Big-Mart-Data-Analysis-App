import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Big Mart operation ")
data_mart=pd.read_csv("ProjectDE/Big Mart.csv")

st.title("Dataset Big Mart ")

col1, col2 = st.columns([1, 3])   
with col2:
    st.image("ProjectDE/BigMart.png",width=300)

info_mart=st.sidebar.checkbox("Info Dataset Big Mart ",False)
describe_mart=st.sidebar.checkbox("Describe Dataset Big Mart",False)
dataset_overview_mart=st.sidebar.checkbox("Dataset Overview  Big Mart",False)
handling_misssing_value_mart=st.sidebar.checkbox("Handling Missing Value Big Mart",False)
statistic_outliers_mart=st.sidebar.checkbox("Statistical Outlier Analysis Big Mart",False)
handling_data_category=st.sidebar.checkbox("Handling Data Type Category",False)
Visualization_data_mart=st.sidebar.checkbox("Visualization data mart",False)

if st.sidebar.button("CLick") :
    
    if info_mart and not(handling_data_category or Visualization_data_mart or describe_mart or dataset_overview_mart or handling_misssing_value_mart or statistic_outliers_mart) :
        st.subheader("DATA SHAPE BIG MART")
        rows_sh,columns_sh=data_mart.shape      
        data_shape_mart={" ": ["Columns","Rows"],
                  "count":[rows_sh,columns_sh] 
                  }
        st.table(pd.DataFrame(data_shape_mart)) # show row and columns
        
        st.subheader("DATA INFO BIG MART")
        data_info_mart = {
       "Column": data_mart.columns,   # name the columns 
       "Non-Null Count": data_mart.notnull().sum().values,    # data not missing value
       "Dtype": data_mart.dtypes.values,  # type the data
        "Null count": data_mart.isna().sum().values
           }     # creat data info 
        st.table(pd.DataFrame(data_info_mart))  
        
    
    elif describe_mart and not(handling_data_category or Visualization_data_mart or info_mart or dataset_overview_mart or handling_misssing_value_mart or statistic_outliers_mart):
        st.subheader("DATA DESCRIBE BIG MART")
        st.table(data_mart.describe())  # show the statistic the data
    
    elif dataset_overview_mart and not(handling_data_category or Visualization_data_mart or describe_mart or info_mart or handling_misssing_value_mart or statistic_outliers_mart):
        st.subheader(" DATA OVERVIEW BIG MART")
        st.table(data_mart)  #  show data
    
    elif handling_misssing_value_mart and not(handling_data_category or Visualization_data_mart or describe_mart or dataset_overview_mart or info_mart or statistic_outliers_mart) :
        st.subheader("HANDLING MISSING VALUE BIG MART")
        t1,t2=st.tabs(["View coumlns handling","View  all data"])
        
        with t1:
             ta1,ta2=st.tabs(["Weight","Outlet Size"])
             st.code("data_mart[Weight].fillna(data_mart[Weight].mean(),inplace=True)")
             data_mart["Weight"].fillna(data_mart["Weight"].mean(),inplace=True)
             st.table(data_mart["Weight"].head(10))
       
                 
             with ta2 :
                 st.code("data_mart [OutletSize].fillna(data_mart[OutletSize].mode()[0],inplace=True)")
                 data_mart ["OutletSize"].fillna(data_mart["OutletSize"].mode()[0],inplace=True)
                 st.table( data_mart ["OutletSize"].head(10))
   
        with t2 :
            st.table(data_mart) 
            
    elif statistic_outliers_mart and not(handling_data_category or Visualization_data_mart or describe_mart or dataset_overview_mart or handling_misssing_value_mart or info_mart):
        t1,t2,t3=st.tabs(["Z-score"," IQR","Handling data outliers"])
        
        with t1:    
            data_mart["Weight"].fillna(data_mart["Weight"].mean(),inplace=True)
            outliers_Weight_z_score=[]
            for i in range(len(data_mart["Weight"])):
                mean_Weight=data_mart["Weight"].mean()
                std_Weight=data_mart["Weight"].std()
                z_score_Weight=(data_mart["Weight"][i]-mean_Weight)/std_Weight
                if abs( z_score_Weight)>3:
                   outliers_Weight_z_score.append(z_score_Weight)
            st.info(f"outliers columns Weight :{len(outliers_Weight_z_score)}")
            plt.figure(figsize=(10,4))
            sns.boxplot(data_mart["Weight"])
            st.pyplot(plt)
            
            outliers_ProductVisibility_z_score=[]
            for i in range(len(data_mart["ProductVisibility"])):
                mean_ProductVisibility=data_mart["ProductVisibility"].mean()
                std_ProductVisibility=data_mart["ProductVisibility"].std()
                z_score_ProductVisibility=(data_mart["ProductVisibility"][i]- mean_ProductVisibility)/std_ProductVisibility
                if abs(z_score_ProductVisibility)>3:
                    outliers_ProductVisibility_z_score.append(z_score_ProductVisibility)
            st.info(f" outliers coulmns ProductVisibility :{len(outliers_ProductVisibility_z_score)}")
            plt.figure(figsize=(10,4))
            sns.boxplot(data_mart["ProductVisibility"])
            st.pyplot(plt)
            
            outliers_MRP_z_score=[]
            for i in range(len(data_mart["MRP"])):
                mean_MRP=data_mart["MRP"].mean()
                std_MRP=data_mart["MRP"].std()
                z_score_MRP=(data_mart["MRP"][i]- mean_MRP)/std_MRP
                if abs(z_score_MRP)>3:
                   outliers_MRP_z_score.append(z_score_MRP)
            st.info(f" outliers columns MRP :{len(outliers_MRP_z_score)}")
            plt.figure(figsize=(10,4))
            sns.boxplot(data_mart["MRP"])
            st.pyplot(plt)

            outliers_EstablishmentYear_z_score=[]
            for i in range(len(data_mart["EstablishmentYear"])):
                mean_EstablishmentYear=data_mart["EstablishmentYear"].mean()
                std_EstablishmentYear=data_mart["EstablishmentYear"].std()
                z_score_EstablishmentYear= (data_mart["EstablishmentYear"][i]- mean_EstablishmentYear)/std_EstablishmentYear 
                if abs(z_score_EstablishmentYear)>3:
                    outliers_EstablishmentYear_z_score.append(z_score_EstablishmentYear)
            st.info(f"outliers columns EstablishmentYear :{len(outliers_EstablishmentYear_z_score)}")
            plt.figure(figsize=(10,4))
            sns.boxplot(data_mart["EstablishmentYear"])
            st.pyplot(plt)
        
        with t2:
            
            rows,cols=data_mart.shape
            st.info(f" data the rows = {rows}")
            data_mart["Weight"].fillna(data_mart["Weight"].mean(),inplace=True)
            Q1_Weight=data_mart["Weight"].quantile(0.25)
            Q3_Weight=data_mart["Weight"].quantile(0.75)
            IQR_Weight=Q3_Weight - Q1_Weight
            upper_Weight=Q3_Weight+(1.5*IQR_Weight)
            lower_Weight=Q1_Weight-(1.5*IQR_Weight)
            dataNormal_Weight=data_mart[data_mart["Weight"].between(lower_Weight,upper_Weight)]
            st.info(f"the count normal data columns Weight used IQR :  {len(dataNormal_Weight)}")

            Q1_ProductVisibility=data_mart["ProductVisibility"].quantile(0.25)
            Q3_ProductVisibility=data_mart["ProductVisibility"].quantile(0.75)
            IQR_ProductVisibility=Q3_ProductVisibility - Q1_ProductVisibility
            upper_ProductVisibility=Q3_ProductVisibility+(1.5*IQR_ProductVisibility)
            lower_ProductVisibility=Q1_ProductVisibility-(1.5*IQR_ProductVisibility)
            dataNormal_ProductVisibility=data_mart[data_mart["ProductVisibility"].between(lower_ProductVisibility,upper_ProductVisibility)]
            st.info(f"the count normal data columns ProductVisibility used IQR :  {len(dataNormal_ProductVisibility)}")
            plt.figure(figsize=(10,4))
            sns.boxplot(data_mart["ProductVisibility"])
            st.pyplot(plt)
            
            Q1_EstablishmentYear=data_mart["EstablishmentYear"].quantile(0.25)
            Q3_EstablishmentYear=data_mart["EstablishmentYear"].quantile(0.75)
            IQR_EstablishmentYear= Q3_EstablishmentYear - Q1_EstablishmentYear
            upper_EstablishmentYear = Q3_EstablishmentYear +( 1.5 * IQR_EstablishmentYear )
            lower_EstablishmentYear = Q1_EstablishmentYear -( 1.5 * IQR_EstablishmentYear )
            dataNormal_EstablishmentYear=data_mart[data_mart["EstablishmentYear"].between(lower_EstablishmentYear,upper_EstablishmentYear)]
            st.info(f"the count normal data columns MRP used IQR : {len(dataNormal_EstablishmentYear)}")
        
            data_mart["MRP"].fillna(data_mart["MRP"].mean(),inplace=True)
            Q1_MRP=data_mart["MRP"].quantile(0.25)
            Q3_MRP=data_mart["MRP"].quantile(0.75)
            IQR_MRP=Q3_MRP - Q1_MRP
            upper_MRP=Q3_MRP+(1.5*IQR_MRP)
            lower_MRP=Q1_MRP-(1.5*IQR_MRP)
            dataNormal_MRP=data_mart[data_mart["MRP"].between(lower_MRP,upper_MRP)]
            st.info(f"the count normal data columns MRP used IQR : {len(dataNormal_MRP)}")
        
        with t3:
            ta1,ta2=st.tabs(["Outliers fixed with IQR method","Outliers fixed with z score method"])
            
            with ta1 :
                for i in range(len(data_mart["ProductVisibility"])):
                    Q1_ProductVisibility=data_mart["ProductVisibility"].quantile(0.25)
                    Q3_ProductVisibility=data_mart["ProductVisibility"].quantile(0.75)
                    IQR_ProductVisibility=Q3_ProductVisibility - Q1_ProductVisibility
                    upper_ProductVisibility=Q3_ProductVisibility+(1.5*IQR_ProductVisibility)
                    lower_ProductVisibility=Q1_ProductVisibility-(1.5*IQR_ProductVisibility)
                    if data_mart["ProductVisibility"][i]> upper_ProductVisibility:
                        data_mart["ProductVisibility"][i]=data_mart["ProductVisibility"].mean()
                    elif data_mart["ProductVisibility"][i]<lower_ProductVisibility:
                        data_mart["ProductVisibility"][i]=data_mart["ProductVisibility"].mean()
                plt.figure(figsize=(10,4))
                sns.boxplot(data_mart["ProductVisibility"])
                st.pyplot(plt)
                plt.figure(figsize=(10,4))
            
            with ta2:
                for i in range(len(data_mart["ProductVisibility"])):
                    mean_ProductVisibility=data_mart["ProductVisibility"].mean()
                    std_ProductVisibility=data_mart["ProductVisibility"].std()
                    z_score_ProductVisibility=(data_mart["ProductVisibility"][i]- mean_ProductVisibility)/std_ProductVisibility
                    if abs(z_score_ProductVisibility)>3:
                        data_mart["ProductVisibility"][i]=data_mart["ProductVisibility"].mean()
                plt.figure(figsize=(10,4))
                sns.boxplot(data_mart["ProductVisibility"])
                st.pyplot(plt)
                
    elif handling_data_category and not (Visualization_data_mart or statistic_outliers_mart or info_mart or describe_mart or dataset_overview_mart or handling_misssing_value_mart):
        data_mart ["OutletSize"].fillna(data_mart["OutletSize"].mode()[0],inplace=True)
        st.subheader(" Handling data type Category ")
        data_mart=pd.get_dummies(data_mart,columns=["FatContent","ProductType"],dtype=("int"))
        data_mart=pd.get_dummies(data_mart,columns=["OutletSize","LocationType","OutletType"],dtype="int",prefix="")
        t1,t2,t3,t4,t5 =st.tabs(["FatContent","ProductType","OutletSize","LocationType","OutletType"])
        
        with t1 :
           st.text (" handling dataset type category coulmn FatContent :")
           st.table(data_mart[["FatContent_LF","FatContent_Low Fat","FatContent_Regular","FatContent_low fat","FatContent_reg"]].head(10))
        
        with t2 :
            st.text (" handling dataset type category coulmn ProductType :")
            st.table(data_mart[["ProductType_Baking Goods","ProductType_Breads","ProductType_Breakfast","ProductType_Canned","ProductType_Dairy","ProductType_Frozen Foods"]].head(4))
            st.table(data_mart[["ProductType_Fruits and Vegetables","ProductType_Hard Drinks","ProductType_Health and Hygiene","ProductType_Soft Drinks"]].head(4))
            st.table(data_mart[["ProductType_Household","ProductType_Meat","ProductType_Others","ProductType_Seafood","ProductType_Snack Foods","ProductType_Starchy Foods"]].head(4))

        with t3:
            st.text (" handling dataset type category coulmn OutletSize :")
            st.table(data_mart[["_High","_Medium","_Small"]].head(10))
            
        with t4:
            st.text (" handling dataset type category coulmn LocationType :")
            st.table(data_mart[["_Tier 1","_Tier 2","_Tier 3"]].head(10))
        
        with t5:
            st.text (" handling dataset type category coulmn OutletType :")
            st.table(data_mart[["_Grocery Store","_Supermarket Type1","_Supermarket Type2","_Supermarket Type3"]].head(10))
    elif Visualization_data_mart :
            st.subheader("Visualization Data Mart")
            t1, t2, t3, t4 = st.tabs(["Numerical Distribution", "Outliers", "Category Analysis", "Correlation"])
            with t1:
                num_cols = ["Weight", "ProductVisibility", "MRP", "EstablishmentYear"]
                for col in num_cols:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    sns.histplot(data_mart[col], bins=30, kde=True, ax=ax)
                    ax.set_title(f"Distribution of {col}")
                    st.pyplot(fig)

            with t2:
                for col in num_cols:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    sns.boxplot(x=data_mart[col], ax=ax)
                    ax.set_title(f"Boxplot of {col}")
                    st.pyplot(fig)

            with t3:
                if "OutletType_Supermarket Type1" in data_mart.columns:
                    cat_cols = ["OutletSize_Small", "OutletSize_Medium", "OutletSize_High","LocationType_Tier 1", "LocationType_Tier 2", "LocationType_Tier 3"]
                else:
                    cat_cols = ["OutletSize", "LocationType", "OutletType"]
        
                for col in cat_cols:
                    if col in data_mart.columns:
                        fig, ax = plt.subplots(figsize=(7, 4))
                        sns.countplot(x=col, data=data_mart, ax=ax)
                        ax.set_title(f"Count of {col}")
                        plt.xticks(rotation=45)
                        st.pyplot(fig)
            with t4:
                fig, ax = plt.subplots(figsize=(8, 5))
                corr = data_mart.select_dtypes(include=["int", "float"]).corr(numeric_only=True)
                sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                st.pyplot(fig)
    else:
        st.warning("There is an error in the selection, please select only one option")

        
