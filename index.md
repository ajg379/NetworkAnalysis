# Determining if Bitcion is becoming a widly used currency.

With the past couple years there have been claims that Bitcion will be the currency to replace modern forms of currency but what would this mean and how is the current transactional history evidence of this.  To keep bias from lerking into my results, except where they tie in, I am going to refrain from talking about other parts of Bitcoin.  

## Brief Introduction to Bitcoin

Before diving into the nitty gritty of my findings, I want to give an overview of how Bitcoin works and the methodology behind it.  Bitcoin is a completely decentralized form of currency with money exchanging hands through the blockchain.  The blockchain is essentially a leger of every single transaction that has every taken place over the Bitcoin network. For this reason, Bitcoin gives the appearance of anononymity while ensuring no single entity controls the balance of the flow of money.  It is secure and distributed becasue of the blockchain but is also a reason why adoption might be low.  Each transaction that orrurs has to go throught a verification process called mining.  Once a transaction has been mined/verified it is added to the blockchain.  When it comes time for results I will go into some depth with reference to the statistics of Bitcoin transaction confirmation so this will be elaborated in the coming sections.  

## Motivation For Analyzing Bitcoin

With a general grasp of how Bitcoin works, I wanted to find out if the Bitcoin network could offer some insight into how the current state of the currency might shed some light on its future.  There is no doubt it is a market disrupter but which market is is disrupting.  Could all the hype surrounding Bitcoin be genuine and it should be taken seriously as a currency or could it be a fallacy that fades away once investor trading dies down?  These questions will only have definitive answers in due time but with Bitcoin being the oldest main stream crypto currency it is a perfect candidate to examine purchasing patterns over the years.  

## Gathering Data

Being an open currency where the blockchain contains every transaction ever made with the currency is publically available, you could imagine the volume of information the blockchain must contain.  If you were to download the entier Bitcoin blockchain, you would need more than 150 Gb of storage space.  My computer has 32 Gb of RAM and unless I want to use paging to virtually increase this to the necessary 150 Gb, there was going to have to be a way to reduce this.  Sampling was inevitebly used. 

A quick aside about a Bitcoin transaction.  Unlike sending $30 from my bank to Whole Foods which has one sender and one receiver, a Bitcion transaction can have multiple senders and multiple receivers.  Knowing this, I wanted to make sure that if a transaction only had one sender or one receiver, the transactions had a higher chance of getting added to the sampled network.  So when iterating through the entire blockchain and all its transactions, the chance a sender being picked was proportional to 1 / (2 * #Senders).  Similarily the chance a sender would be picked was 1 / (2 * #Receivers).  So if there was 1 sender and 10 receivers.  The receiver would have a 50% chance of being selected and any one of the receivers would have a %5 chance of being selected.  

This sampling technique does not have an effect of the trends that would emerge from the network.  For instance, a transaction from 1 sender to 1 receiver would not be disproportitely represented in the network since these are on the transaction level not the overall degree level.  I wish I could have included more nodes in the network but unfortunately even storing only the sender and receiver as integers was still on the order of Gb's for the sample from 2017.  My sampling technique was effective in reducing the dataset to a managable level, around 500 Mb for 2017.  I know what you might be thining, "You have 32 Gb of RAM why can't you handle a larger dataset".  While it would make sense that with this level of data I could import a much larger subset of the Bitcoin netowrk, when loading the edge list into NetworkX, that 500Mb edge list turns into a 29 Gb NetworkX object and taking into account other OS processes, all my RAM gets taken and paging starts.  With all this being said sampling was successful and I got as much data as I could given restrictions. 

From 



The innerworking of Bitcion are closely related to other forms of crypto currencies but the track recor






You can use the [editor on GitHub](https://github.com/ajg379/NetworkAnalysis/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ajg379/NetworkAnalysis/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
