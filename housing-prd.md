### What problem are we tackling?
It seems like housing should be a pretty solved market. Given certain characteristics of a property, we should be able to deduce a fair price based on historical sales. However, when walking around an open house, it's hard (for me, at least!) to deduce whether the price is fair, or whether it's over-priced (or under-priced). It makes an already scary process (buying a house) even more uncertain. And, this is exacerbated by realtors who will very confidently say "yes, this is over-priced" or "this is a fair price", without providing any data. Which leads to another pain point: finding and selecting a realtor is hard. Sure, some of it is emotional - 'who do i want to spend a shit ton of time with and who do i innately trust?' But, as a Data Science person, I need to use some data here. I want to know how well realtors have negotiated, if they've actually worked on deals like we're looking for, etc. 

### What is the high level approach we'll take? 
The real estate market provides a ton of data. We can use this data to build a set of models that can help us assess the fair price (or expected price) of a property given a set of characteristics. We will leverage a few data sources: 
- rentcast.io API - this will give us real-time information about properties currently listed on the market as well as detailed property information for both active listing (i.e., for sale) and inactive listings (i.e., not on the market)

- Zillow static data files (updated monthly) - this is a set of ~15 - 20 static CSV files that provide information about trends. Things like available inventory by market by week, average days to pending by week in each market, etc. 

- Boulder County Real Estate Transaction reporting (CSV file, updated monthly) - this is a detailed record of RE transactions in Boulder County. This includes realtor data, which may help us in assessing which realtor to proceed with. 

### What are our goals here? 
1. This model will help us (and eventually, hopefully, customers) understand where there is value in the real-estate market for a given region. I want to produce a data science framework that will help us say "yep - this house is way over priced, let's wait or pass." There is a ton of emotion in real estate - and that's fine, but we are also keen on making a solid investment. And as such, want to treat this as we would with any investment - which is, dig into the data and identify mispriced assets. 
2. I want us to be able to make a (somewhat) data-driven approach in choosing a realtor. How do we go from "yes I've got a lot of experience working on what you're looking for" to actually understanding their transaction history and outcomes. 
3. I want to productionize these models. A parallel project is to build a web app where a user can see all active listings for an area (or areas), and maintain a list of properties they're excited about. This will also be AI-informed, with users giving criteria (e.g., 4+ beds, 3+ baths, garage) and an LLM using that to parse listing data and surface listings with a >x% match. As part of this web app, I want to build a 'Market Sage' module, where users can assess the price quality of a listing - so that they too can understand whether a price is too high / low / or fair. 
4. I'm working on a transition right now in my career to AI/ML Product Management OR actual Data Science. I'm using this as one of the core projects to gain experience and demonstrate technical capability. 

### What are the requirements? 
**DATA & MODELING**
1. We will build automated data pipelines for both the API connections as well as static data connections. 
	1. For API connections, we will refresh the data 1x per day. 
	2. For static data connections, we will refresh the data on the given schedule by the provider. Zillow will refresh on the 16th of each month, and Boulder County static data will refresh on the 5th of the month. 
2. We will write and store data to databases, not local files. This will be a topic for us to deep-dive. I am not sure yet where I want to go from an architecture perspective -- deciding if I should go straight to something like GCP to start, or start with a different DB product and then migrate to GCP later. 
	1. Cost is a major consideration - I'm willing to spend a little bit for optimized performance and to demonstrate capabilities in different tech for my portfolio, but am not generating revenue here. 
3. We should consider whether machine learning techniques should be used - and if so, we should certainly use them. 
4. We should be utilizing testing to ensure robustness and accuracy of our model, and we should be tracking and displaying our model accuracy metrics clearly on the UI. 

**UI AND VIZ**
1. There should be a clean UI, that is not cluttered and does not contain a bunch of excess features, pages, buttons, etc. 
2. Use the attached screenshots as inspiration for the UI / Design style that I really like. 



