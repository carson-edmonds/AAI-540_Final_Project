# AAI-540_Final_Project
Software bots have increased in popularity on bidding sites due to their ability to outbid and win auctions against humans. This in turn reduces the human satisfaction with online auctions and causes a site’s customer base to decrease. To rebuild the customer base it is important to identify computer generated bidding so that they can be removed and deter unfair auction activity. This can be completed using machine learning techniques to classify online auction bids as either human or bot. This analysis is based on data provided in the Facebook Recruiting IV: Human or Robot dataset on [Kaggle](https://www.kaggle.com/competitions/facebook-recruiting-iv-human-or-bot/data) (Facebook, 2015). The data is collected from 7.6 million bids made on mobile devices at different auctions and includes data such as the bidder’s country of origin, address, and payment account.

The steps for this analysis are as follows:  
- S3 datalake creation
- Data exploratory analysis
- Feature engineering
- Model training and evaluation
- Model deployment and monitoring
- CI/CD pipeline implementation

To run the analysis, run notebooks in numerical order. 

References:
Facebook (2015). Facebook Recruiting IV: Human or Robot? [Data set]. Kaggle. https://www.kaggle.com/competitions/facebook-recruiting-iv-human-or-bot/overview 
