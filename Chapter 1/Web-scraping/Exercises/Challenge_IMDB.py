from selenium import webdriver
from time import sleep
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px

def web_extraction():
    movie_names = []
    release_date = []
    description = []
    directors = []
    movie_stars = []
    ratings = []
    duration = []
    genre = []

    url = 'https://www.imdb.com/list/ls009668711/?sort=moviemeter,asc&st_dt=&mode=detail&page=1';
    pth = 'chromedriver.exe'

    driver = webdriver.Chrome(pth)

    driver.get(url)
    
    sleep(20)

    movies = 100
    for i in range(1,movies+1):
        
        movie = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/h3/a')
                                    
        release = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/h3/span[2]')

                                                 
        desc = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[2]')
                                                
        dire = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[3]/a[1]')

        rat = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/div[1]/div[1]/span[2]')

        dura = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[1]/span[3]')

        gen = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[1]/span[5]')
                                            
        movie_ = movie.text
        movie_names.append(movie_)
        
        whole = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[3]')
        whole_ = whole.text
        director, space, stars = whole_.partition('Stars: ')
        movie_stars.append(stars)
    
    
        release_ = release.text
        find_wo_brackets = release_.replace('(','')
        find_wo_brackets = find_wo_brackets.replace(')','')

        if i == 70:
            find_wo_brackets = 2015
        if i == 76:
            find_wo_brackets = 2004
        if i == 93:
            find_wo_brackets = 2006
        release_date.append(int(find_wo_brackets))

        description_ = desc.text
        description.append(description_)

        directors_ = dire.text
        directors.append(directors_)

        ratings_ = rat.text
        int_ratings_ = float(ratings_)
        ratings.append(int_ratings_)

        duration_ = dura.text
        durat, space, stri = duration_.partition(' ')
        int_duration = int(durat)
        duration.append(int_duration)

        genres_ = gen.text
        genre.append(genres_)

#########################################       SAVING IT INTO PANDAS DATAFRAME        #######################################################################
  
    data = {'Movies':movie_names,'Description':description,'Directors':directors,'Movie Stars':movie_stars,'Genre':genre,'Release Date':release_date,'Duration (in mins)':duration,'Ratings':ratings}
    
    
    
    labels = pd.RangeIndex(start=1,stop=movies+1,step=1)
    
    df = pd.DataFrame(data,index =labels).rename_axis('Serial Number',axis=1)
    df.to_csv('drama_imdb.csv')
    
    return df

def preprocessing():
    data = pd.read_csv('drama_imdb.csv',index_col=0)
    
    return data


def best_actor(movie_stars,data):
    return data[data['Movie Stars']==movie_stars].sort_values("Ratings",ascending=False)['Movies'].head(1).item()

def min_max_normalization(df,name_of_column,variable):

    df_norm = df.copy()
    # apply min-max scaling
    df_norm[name_of_column] = 1 + ((df_norm[variable] - df_norm[variable].min()) / (df_norm[variable].max() - df_norm[variable].min())) * 9
    return df_norm

def mean_normalization(df,name_of_column,variable):
    # copy the dataframe
    df_norm = df.copy()
    # apply mean scaling
    df_norm[name_of_column] = 1 + ((df_norm[variable] - df_norm[variable].mean()) / (df_norm[variable].max() - df_norm[variable].min())) * 9
    return df_norm


def streamlit_template(graphs,data):  #streamlit_template(graphs, data)

    #st.set_page_config(layout="wide")
    st.sidebar.markdown("<h1 style=' color: #948888;'>Challenge Day</h1>",
                        unsafe_allow_html=True)
    st.sidebar.write('\n')
    st.sidebar.header("""**Contributors:**""")
    st.sidebar.write("\t  > Shahiq ")
    st.sidebar.write("\t  > Abubakr")

    st.sidebar.write('\n')   
    st.sidebar.header("**Objectives:**")
    
    
    st.sidebar.write("""
                    > 1. Scraping the top 100 Drama Movies from IMDB.

                    > 2. Preprocessing the data for better analysis, by transforming the data with normalization.

                    > 3. Visualizing the data using matplotlib and seaborn.

                    > 4. Publishing the results using streamlit with the help of plotly.
""")


    img1 = Image.open("imdb.png")
    st.image(img1)     
    st.title("IMDB's Top 100 Drama movies")

    st.header("Data Collection:")

    # data['Movies'] = data["Movies"].astype(str)
    # data['Description'] = data['Description'].astype(str)
    # data['Directors'] = data['Directors'].astype(str)
    # data['Movie Stars'] = data['Movie Stars'].astype(str)
    # data['Genre'] = data['Genre'].astype(str)
    # data['Release Date'] = data['Release Date'].astype(int)
    # data['Duration'] = data['Duration'].astype(int)
    # data['Ratings'] = data['Ratings'].astype(float)



    data = min_max_normalization(data,'MinMax_Norm_Ratings','Ratings')

    data = min_max_normalization(data,'MinMax_Norm_Duration (in mins)',"Duration (in mins)")

    data = mean_normalization(data,'Mean_Norm_Ratings',"Ratings")

    data = mean_normalization(data,'Mean_Norm_Duration (in mins)',"Duration (in mins)")
      
    if st.checkbox("Show the data with minmax normalization and mean normalization."):
        norm = st.dataframe(data)



def graphs(data):
    
    #Graph 1
    
    st.write('\n')
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  

    original_title1 = '<p style="font-family:Times New Roman; color:Blue; font-size: 24px;">Relationship of Ratings over Released Years</p>'
    st.markdown(original_title1, unsafe_allow_html=True)
    df_graph = pd.read_csv('graph1.csv')
    fig_ratings = px.scatter(df_graph, x = "Released Year", y = "Ratings", color = "Ratings",color_discrete_sequence=px.colors.qualitative.Prism,width=850, height=500)
    fig_ratings.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 1940,
        dtick = 10 
    ))
    fig_ratings.update_yaxes(range=[0,10])
    st.plotly_chart(fig_ratings)
    st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 18px;"> In the early years, less movies were released can be due to less technological advancements.                                                                                                                  From 1990, more top drama movies were released can be progressive change in camera, software developments etc.</p>',unsafe_allow_html=True)
    st.text(' ')
    st.text(' ')


    # Graph 2

    st.write('\n')
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    original_title2 = '<p style="font-family:Times New Roman; color:Blue; font-size: 24px;">Number of movies directed by each director</p>'
    st.markdown(original_title2, unsafe_allow_html=True)
    fig_directors = px.histogram(data,x='Directors',width=850, height=500,color = "Directors",color_discrete_sequence=px.colors.qualitative.D3)

    st.plotly_chart(fig_directors)

    st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 18px;"> Martin Scorsese directed 6 movies and Alejandro G. directed 5 movies which were among the top 100 Drama Movies.                                                                                                                                                                                                                                 Most of the directors had directed only one movie and were among the top 100 Drama Movies.</p>',unsafe_allow_html=True)
    st.text(' ')
    st.text(' ')
    st.write('\n')
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    st.write('\n')  
    d = pd.read_csv('actors.csv')
    original_title3 = '<p style="font-family:Times New Roman; color:Blue; font-size: 24px;">Number of movies played by each Star</p>'
    st.markdown(original_title3, unsafe_allow_html=True)
    fig_actors = px.histogram(d,x='Movie Stars',width=850, height=500,color = "Movie Stars",color_discrete_sequence=px.colors.qualitative.T10)
    st.plotly_chart(fig_actors)


    st.markdown('<p style="font-family:Times New Roman; color:Black; font-size: 18px;"> Leonardo DiCaprio, Al Pacino has played the movie star role 7 times in Top 100 Drama Movies.                        \n                                                                                                                                                                                                        Most of stars had played the movie star role atleast once in the top 100 Drama Movies.</p>',unsafe_allow_html=True)

    st.text(' ')
    st.text(' ')


if __name__ == "__main__":
    
    data = preprocessing()
    
    streamlit_template(graphs,data)
    graphs(data)