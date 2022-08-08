# Avaya OneCloud CPaaS with ALE OmniSwitch
Unleash the power of Avaya OneCloud CPaaS together with ALE OmniSwitch

# Usage
- Clone the repository
- Edit the **mysecrets_template.py** and save it as **mysecrets.py**
  - Adapt the **baseURL** (if needed for your region, refer to Avaya CPaaS documentation)
  - Add your **accountSID** (available from Avaya CPaaS Dashboard)
  - Add your **authToken** (available from Avaya CPaaS Dashbboard)
  - Adapt **toNbr** and **fromNbr** depending on your needs (TO which number should the SMS be sent? FROM which number?)
- Upload the Python files to your ALE OmniSwitch and associate Event-Action or CRON-Events, depending on your needs 

# Diagram
<img width="960" alt="API-UseCases-ALE-OmniSwitch" src="https://user-images.githubusercontent.com/5174414/183359206-dc0607ef-cab4-48b2-9914-5455a2393719.png">
