# Avaya OneCloud CPaaS with Alcatel-Lucent Enterprise OmniSwitch
Unleash the power of <a href="https://www.avaya.com/en/products/cpaas/">Avaya OneCloud CPaaS</a> together with <a href="https://www.al-enterprise.com/en/products/switches">Alcatel-Lucent Enterprise OmniSwitch</a>

# Usage
- Clone the repository
- Edit the **mysecrets_template.py** and save it as **mysecrets.py**
  - Adapt the **baseURL** (if needed for your region, refer to <a href="https://docs.avayacloud.com/aspx/rest">Avaya OneCloud CPaaS documentation</a>)
  - Add your **accountSID** (available from Avaya OneCloud CPaaS Dashboard)
  - Add your **authToken** (available from Avaya OneCloud CPaaS Dashbboard)
  - Adapt **toNbr** and **fromNbr** depending on your needs (TO which number should the SMS be sent? FROM which number?)
- Upload the Python files to your ALE OmniSwitch and associate Event-Action or CRON-Events, depending on your needs 

# Diagram
<img width="960" alt="API-UseCases-ALE-OmniSwitch" src="https://user-images.githubusercontent.com/5174414/183359206-dc0607ef-cab4-48b2-9914-5455a2393719.png">
