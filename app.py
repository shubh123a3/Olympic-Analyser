import streamlit as st
import plotly.express as px
import pandas as pd
import prepocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df=prepocessor.preprocess()
st.sidebar.title('Olympics Analysis')
st.sidebar.image("assets/img.png", use_column_width=True)
user_menu=st.sidebar.radio('select an option',('Medal Tally','Overall Analysis','Country-wise analysis','Athlete Wise Analysis'))

if user_menu=='Medal Tally':
    st.sidebar.header('Medal Tally')
    years,country=helper.country_year_list(df)
    selected_year=st.sidebar.selectbox('selected years',years)
    selected_country = st.sidebar.selectbox('selected country', country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country )
    if selected_year=='Overall' and selected_country=='Overall':
        st.title('Overall Medal Tally')
    if selected_year!='Overall' and selected_country=='Overall':
        st.title("%d  Medal Tally"%selected_year)
    if selected_year=='Overall' and selected_country!='Overall':
        st.title(selected_country+' Overall Medal Tally')
    if selected_year!='Overall' and selected_country!='Overall':
        st.title('%d Medal Tally of %s'%(selected_year,selected_country),)
    st.table(medal_tally)


if 'Overall Analysis' == user_menu:
    editions = df['Year'].nunique() - 1
    cities = df['City'].nunique()
    sports = df['Sport'].nunique()
    events = df['Event'].nunique()
    athletes = df['Name'].nunique()
    nations = df['region'].nunique()
    st.title('Top Statistcs')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Host Cities')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.header('Events')
        st.title(events)
    with col5:
        st.header('Athletes')
        st.title(athletes)
    with col6:
        st.header('Nations')
        st.title(nations)
    nation_over_time=helper.participating_nation_over_time(df)
    st.title('Participation of Nation')
    fig = px.line(nation_over_time, x="Year", y="count")
    st.plotly_chart(fig)
    #number of event
    st.title('Total number of event')
    total_event= df.drop_duplicates(['Year', 'Event'])['Year'].value_counts().reset_index().sort_values('Year')
    fig_event = px.line(total_event, x="Year", y="count")
    st.plotly_chart(fig_event)
    #njumber of Athlete
    st.title('Total number of Athlete')
    total_Athlete = df.drop_duplicates(['Year', 'Name'])['Year'].value_counts().reset_index().sort_values('Year')
    fig_Athlete = px.line(total_Athlete, x="Year", y="count")
    st.plotly_chart(fig_Athlete)
    #heat_map
    st.title('No. of Events Overtime (Every Sport)')
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax=sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
                annot=True)
    st.pyplot(fig)
    #total
    st.title('most successful athletes')
    sport_list=df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport=st.selectbox('Select Sport',sport_list)
    x=helper.most_succesful(df,selected_sport)
    st.table(x)
if 'Country-wise analysis' == user_menu:
    st.sidebar.title('Country-wise analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    select_country=st.sidebar.selectbox('Select Country',country_list)
    new_df = helper.year_wise_medal_tally(df, select_country)
    fig_year = px.line(new_df, x="Year", y="Medal")
    st.title(select_country+' Medal tally over year')
    st.plotly_chart(fig_year)
    #heatmap
    st.title(select_country + ' Excel in following Sports')
    fig, ax = plt.subplots(figsize=(20, 20))
    x=helper.Country_event_heatmap(df, select_country)
    ax=sns.heatmap(x, annot=True)
    st.pyplot(fig)
    #countrywise
    st.title(select_country + 'TOP 10 Athletes ')
    temp_df=helper.most_succesful_region(df,select_country)
    st.table(temp_df)

if user_menu=='Athlete Wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_rug=False, show_hist=False)
    fig.update_layout(autosize=False ,width=1000,height=600)
    st.title('Distribution of Age of Athletes')
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports=['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
    'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
    'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
    'Water Polo', 'Hockey', 'Rowing', 'Fencing',
    'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
    'Tennis', 'Golf', 'Softball', 'Archery',
    'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
    'Rhythmic Gymnastics', 'Rugby Sevens',
    'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fig = ff.create_distplot(x, name, show_rug=False, show_hist=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title('Distribution of Age of Athletes who has won the Gold Medal')
    st.plotly_chart(fig)

    st.title('Distribution of Age of Athletes Weight and Height')

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select Sport', sport_list)
    temp_df = helper.weight_hight_age(df, selected_sport)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax=sns.scatterplot(data=temp_df,x='Weight',y='Height',hue='Medal',style='Sex',s=100)
    st.pyplot(fig)
    st.title('Men Vs Women Participation Over the Years')
    final=helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
























