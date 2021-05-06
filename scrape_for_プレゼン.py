import twint

c = twint.Config()
c.Username = "ayanami_rei_T"
c.Output = "tweets.json"
c.Store_json = True
twint.run.Search(c)















