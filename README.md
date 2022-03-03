# StockMarket
2020 StockMarket Project
Below is a writeup of our logic behind the code.
Nicholas Kantarellis / Dongmin Li
Abstract

The Stock Market today is a huge component of business and people are constantly looking for ways to monitor their stocks. These people always wonder when they should be actively buying stocks or even when they should be selling their stocks at a high. There are various ways to help investors making their decisions. However, lots of ways are quite complicated for they utilize financial engineering or complicated mathematical models, which makes investors confused about which to choose. Since many factors will affect the performance and investors are risk averse, it leads to a simple but straight method to help investors decide which stock to invest, the Risk Aversion Function, according to their own risk tolerance and stock expected return. We develop a simple but straight investment decision helper based on python where our users can input several necessary information for each stock in a notepad and by importing the data, the program will do some calculations to give users a suggestion which stock has the priority. Our program will display a projection of each stock through a graph and it will then let the user know which stock will hold the most utility value. In future work, we will work on improve the efficiency of collecting data, and taking more factors into consideration to make the result more accurate.

Introduction

People who invest are faced with many decision makings, to determine which to choose, when to invest and how much risk to take. According to a survey held in 2017 that explores more than 22,000 people who invest globally about their understanding and behaviors (Global Investor Study 2017, Investor behavior: from priorities to expectations, by Schroders), 88% of

people feel that they need to enhance their investment knowledge, and nearly a quarter intend to invest in securities such as stocks, or bonds, which is relatively risky. And surprisingly, most people seem to hold an unrealistically high expectations about their investment (10.2% per year over the next five years) while the significant role that plays in how people make decisions about finance is emotion. Obviously, people are quite confused about making investment decisions, when they are faced with a large variety of investment. Therefore, it grows rapidly for the demand to help investors make their decisions.

To predict the actual return on a specific stock or portfolio requires much work on data analysis. Many factors, like the market return, random event or policies, will have a tiny or great impact on the stock market. There are many ways to do the security analysis, in order to find the optimal portfolio about the stock selection. We have ways like Markowitz model, which requires the correlation for each stock to be known, or Sharpe’s single factor model, which is less complicated but requires much data to calculate that is unrealistic for an individual investor to acquire. To simplify the solution without losing the basic function that could help the investors make their own decisions, we focus on two main factors, risk aversion and expected return, that lead to the Utility Score, a mathematical device for ranking investment.

Background

Investors have the unwillingness to risk investment, unless the investment could provide the extra expected return with an acceptable level of risk. A high value of risk aversion indicates low risk tolerance, which means, the person is unwilling to afford much risk. Those people are more willing to put their money in bank account with a low promised interest rate, rather than invest in stock market, which may provide high returns, but also contains risk of losing money. Therefore, we use the utility score function to evaluate the risk and expected return as following: 𝑼=𝑬(𝒓)−𝟏𝟐𝑨𝝈𝟐

U: Utility score;

E(r): Expected return;

A: Risk aversion degree (range from 1 to 10);

σ: Standard deviation

This is one plausible form among other functional choices of utility function. Investors only need to know the standard deviation and expected return from their investment and his or her tolerance to risk, then he could rank the investment according to the utility score, the higher the more priority.

Method

Conclusion

By simulation, we discover the advantages as well as the disadvantages our program holds as follows:

Advantages

1. It’s simple but effective to deal with, and it could be used by those who have little investment knowledge.

2. It focuses the factors only on risk aversion and expected return, which are factors accessible for individual investors.

3. It gives a ranking to different investment by sorting the utility scores from the highest to the lowest, which helps investors to determine the priority of their investment.

4. It’s applicable for both people who are unwilling to take risk and people who seek more profits with taking risk.

Disadvantages

1. It fails to take the market performance into account, which might place the investors to the exposure of global risk.

2. The equal utility scores may occur which indicates a indifference between two stocks that lead to the hesitation of investors to make their decision and they have to consider other factors.

3. It gives no suggestions on the portions to invest, which means diversification is poorly considered.

We found that this program brings a simple and straight guidance to people with little investment knowledge, considering their risk tolerance. But we have to take other factors into consideration as well. To improve our program, other factors should be taken into the

function so that we could reach a more accurate and feasible conclusion to guide investors. Moreover, we use text file to import the data which requires much pre-work to input data, if there are multiple stocks. We may figure out other ways to collect the data automatically from websites, which would definite reduce the work for input.

Reference

Global Investor Study 2017, Investor behavior: from priorities to expectations, issued by Schroders. Retrieved from https://www.schroders.com/en/sysglobalassets/digital/insights/2017/pdf/global-investor-study-2017/theme2/schroders_report-2__eng_master.pdf

Investopedia, https://www.investopedia.com/terms/r/riskaverse.asp
