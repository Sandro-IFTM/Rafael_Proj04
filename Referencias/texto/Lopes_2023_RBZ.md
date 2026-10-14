# Lopes_2023_RBZ

- Arquivo: `Referencias/Lopes_2023_RBZ.pdf`
- Páginas: 21
- Fonte oficial para citação: o PDF (conferir página e trecho literal nele).

=== pág. PDF 1 | rótulo - ===

R. Bras. Zootec., 52:e20210227, 2023 https://doi.org/10.37496/rbz5220210227

Animal production systems and agribusiness

Full-length research article

Brazilian Journal of Animal Science e-ISSN 1806-9290 www.rbz.org.br

Jusecléia Ferreira Lopes1 , Maria Eugênia Andrighetto Canozzi2 , Thaís Lopes Gonçalves3 , Marcela Kuczynski da Rocha1 , Everton Dezordi Sartori1 , Amir Gil Sessim1 , Izabela de Paula Pereira1 , Luis Kluwe de Aguiar4 , Dimitrios Paparas5 , Silvio Renato Oliveira Menegassi1 , Celso Koetz Junior6 , Ricardo Pedroso Oaigen3 , Daniele Zago1 , Júlio Otávio Jardim Barcellos1*

1	 Universidade Federal do Rio Grande do Sul, Departamento de Zootecnia, Porto Alegre, RS, Brasil. 2	 Instituto Nacional de Investigación Agropecuaria, La Estanzuela Experimental Station, Colonia, Uruguay. 3	 Universidade Federal do Pampa, Uruguaiana, RS, Brasil. 4	 Harper Adams University, Department of Food Science and Agrifood Supply Chain Management, Newport, Shropshire, United Kingdom. 5	 Harper Adams University, Food, Land and Agribusiness Management Department, Newport, Shropshire, United Kingdom. 6	 Universidade Norte do Paraná, Arapongas, PR, Brasil.

*Corresponding author: julio.barcellos@ufrgs.br

Received: December 17, 2021 Accepted: February 2, 2023

How to cite: Lopes, J. F.; Canozzi, M. E. A.; Gonçalves, T. L.; Rocha, M. K.; Sartori, E. D.; Sessim, A. G.; Pereira, I. P.; Aguiar, L. K.; Paparas, D.; Menegassi, S. R. O.; Koetz Junior, C.; Oaigen, R. P.; Zago, D. and Barcellos, J. O. J. 2023. Price determinants of beef bulls sold in livestock auctions. Revista Brasileira de Zootecnia 52:e20210227. https://doi.org/10.37496/rbz5220210227

Copyright: This is an open access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

ABSTRACT - The main objective of this study was to evaluate the effects of phenotypic, genotypic, and auction characteristics that may influence the selling prices of bulls. Data from 1,540 Braford and 1,179 Brangus bulls sold at auctions in the state of Rio Grande do Sul, Brazil, were collected and evaluated individually. Body condition score (BCS), muscularity, frame, foreskin size, presence or absence of horns, and data regarding the auction such as name/venue, event edition, forms of payment, among others, were considered. Information such as weight at the time of sale, scrotal circumference (SC), expected profit differences, selection indexes, and date of birth were collected from the catalogs supplied at the auctions. To obtain the influence of the selected explanatory variables throughout the conditional distribution of bull prices, a quantile regression was used, and the quantiles were established as follows: 10th, 25th, 50th, 75th, and 90th. The buyers of Braford and Brangus bulls valued characteristics such as age, weight, and SC in relation to frame, muscularity, BCS, and foreskin size. In addition, the price behavior at different auctions was positively related to the operation time of the auction in this market and with the reputation of the seller. Regarding genetic variables of Brangus bulls, these had little or no influence on the selling price. There was a positive influence on the weaning index in the 90th quantile and on the final index in the 50th and 75th quantiles. Buyers of synthetic bull breeds at auctions value the phenotypic characteristics of bulls more than they do genetic characteristics, which may not reflect permanent gains in the cattle herd.

Keywords: animal production, beef cattle, marketing, phenotypic variation

1. Introduction

In cow-calf systems, natural mating has been the predominant breeding method, used approximately in 80% of the beef cow population in the world (Thibier and Wagner, 2002). Usually, farmers tend

=== pág. PDF 2 | rótulo - ===

to select bulls for replacement, especially certified bulls from cattle breeders associations during livestock auctions. Synthetic breeds, such as Braford, Brangus, Santa Gertrudis, Montana, Blonde D’aquitaine, and others, are very important as they cater for an increasing demand for biotypes adapted to tropical conditions (Menegassi et al., 2016) as well as their potential for the improvement of beef quality (ABHB, 2018).

Braford and Brangus herd sizes are usually made available from the respective cattle breed associations. Despite this, they are not always disclosed, and it is thus estimated that the Hereford and Braford herds in Rio Grande do Sul, Brazil, is approximately 1.8 million head, approximately representing 20% of total cattle herd of that state. As for the Brazilian Brangus herd, it has increased by 80% in the last decade (ABB, 2022). The Braford breed originated from a cross between the Hereford × Brahman or Hereford × Zebu breeds (ABHB, 2023), and Brangus originated from a cross between the Brahman × Angus or Angus × Zebu (ABB, 2022).

To better explore the potential of synthetic breeds, it is important to buy bulls with characteristics aligned with the production system and the market. The price of bulls is related to several factors that can maximize production, such as breed, conformation, appearance, age, weight at the time of sale, frame, expected progeny difference (EPD), and place of sale (Commer Jr. et al., 1990; Dhuyvetter et al., 1996; Jones et al., 2008). However, it is important to analyze the extremes of the sale price, seeking to understand how and with what intensity the different variables change it.

Studies in this area traditionally analyze the relationship between the average of the dependent variable (price) and independent variables (breed, conformation, appearance, age, weight, frame, EPD, among others). The ordinary least squares statistical methodology has been used in previous studies to compare the value of production weights (birth, weaning, and yearling weight), production expected (EPD of birth, weaning, milk, and yearling), bull color, polled, conformation, muscularity, disposition, age, sale location, bull sale order, whether the bull had a picture in the sale catalog, and whether a percentage of semen rights was retained by the seller, and ultrasound EPD (carcass quality predictors) for purebred bulls sold at auctions (Dhuyvetter et al., 1996; Jones et al., 2008). However, most of these studies consider only the average in the evaluation of the relationship between bull price and the variables of interest, not measuring the behavior in the tail of the distribution or points of interest. The current study used a quantile regression (QR) to evaluate the price determinants in the tail of the distribution, especially when the conditional distribution showed an asymmetric shape.

The QR allows for a complete characterization of the effect caused by the phenotypic variables, as well as the marketing factors that can influence the price paid per animal, mainly when the price of a bull shows a considerable amplitude. The QR informs the price determinants that influence the smaller, median, and the greatest price, regarding the conditional price distribution, according to method of Koenker and Bassett (1978).

The interest in synthetic breeds in a Brazilian context is because they meet the new demands of the consumer market and the potential for meat production. Therefore, it is felt that information on the commercialization of synthetic bulls at auctions is essential to allow for animals of proven genetics that deliver good-quality meat production and that are adapted to the tropical climate. The main objective of the current study is to attempt to close the gap in the understanding of the relationships and main characteristics that influence the prices of Braford and Brangus bulls sold in auctions.

2. Material and Methods

In this study, we used data from 2,719 bulls of the Brangus and Braford breeds sold at auctions in the state of Rio Grande do Sul, Brazil, from 2013 to 2017. The events are usually organized by auction companies, cattle farmers’ associations, or by the Hereford and Braford or Brangus Breed Association, taking place at the association or on private farms. The data were collected by trained researchers with experience in the phenotypic evaluation of animals. The variables collected were pre-selected based on a literature review (Dhuyvetter et al., 1996; Jones et al., 2008).

=== pág. PDF 3 | rótulo - ===

The data collection was carried out in three stages (Table 1):

Before the bulls entered the ring, they were individually evaluated, and information including the animal ID, presence or absence of horns (POLLED), and the frame (FRAME), muscularity (MUSC), body condition (BCS), and sheath (SHEATH) scores were collected.

As for FRAME, scores from 1 to 3 were given according to the height measured from the hip of the animal, as proposed and adapted from BIF (1986). A FRAME of 1 represented a height from 104 to 114 cm, typically of smaller biotypes; a FRAME of 2 ranged from 119 to 129 cm in height, representing biotypes of average height; and a FRAME of 3 represented the large biotype (> 129 cm).

Regarding MUSC, bulls were classified according to their score on a scale of 1 to 3 (McKiernan, 2007), in which a MUSC of 1 represents individuals with a concave muscular profile, narrow width between the hind legs, prominent hip bone, and tapered thighs; a MUSC of 2 is typical of average muscularity,

Table 1 - Variables evaluated in Brangus and Braford bulls sold at auctions in Rio Grande do Sul State, Brazil

Variable Definition Unit/ value

Braford variables

Brangus variables

Animal information (before auction)

AGE Age of bulls Months Yes Yes

POLLED Polled binary variable = 1 if bull is polled; otherwise = 0 0-1 Yes No

FRAME Frame score (1 = smaller to 3 = larger) 1-3 Yes Yes

MUSC Muscularity score (1 = poorest to 3 = best) 1-3 Yes Yes

BCS Body condition score (1 = poorest to 5 = best) 1-5 Yes Yes

SHEATH Sheath score (1 = smaller to 3 = bigger) 1-3 Yes Yes

WEIGHT Weight at sale kg Yes Yes

SC Scrotal circumference cm Yes Yes

EPDBW (auctions A and B) Expected progeny difference for birth weight kg No Yes

EPDBTW (auction B) Expected progeny difference for weight gain from birth to weaning kg No Yes

IWean (auction A) Selection indexes for weaning - No Yes

IFinal (auction A) Selection indexes final - No Yes

Auction information (during auction)

AUCTION Auction binary variables: 1 = if bull is that auction; otherwise = 0 (Auction M: default) 0-1 Yes Yes

Number of editions Number of auction editions 0 to 50 Yes Yes

Marketing strategies Marketing strategies used to advertise the event - Yes Yes

Name of the sellers Name of the farm that sells the bull - Yes Yes

Payment conditions Payment in full or in installments - Yes Yes

Post-sale warranty Warranty provided by the bull seller - Yes Yes

Media broadcasting Broadcast by TV or internet - Yes Yes

Bank credit Purchase made through bank credit Yes or no Yes Yes

Free delivery Possibility of free delivery Yes or no Yes Yes

Year Year 2013 (default), 2014 and 2015 Yes No 2014 to 2017 No Yes

Sales data (during auction)

ORDER The order in which bulls are presented for sale at the auction - Yes No

Ring time Time in the ring Seconds Yes No

Final sale price - US$ Yes Yes

Buyer’s name - - Yes Yes

Place of bull destination - - Yes Yes

=== pág. PDF 4 | rótulo - ===

muscular profile that is less convex, and with hip bones slightly prominent; and a MUSC of 3 represents animals with better muscularity, convex muscular profile, large width between the hind legs, well-rounded top line, and thicker thighs.

Body condition score from 1 to 5 (adapted from Lowman et al., 1976) was given to individuals according to the following: BCS of 1 was for very thin individuals, with ribs and some muscle still visible, and easily visible back; a BCS of 2 represented lean bulls that were thin, with ribs easily visible but shoulders and hind quarters still showing fair muscularity; bulls with a BCS of 3 had some fat deposition in the brisket and over the tailhead and ribs, and their back appeared rounded; a BCS of 4 represented bulls of good muscular cover that had some fat cover; and a BCS of 5 were typical of bulls with excess fat cover at the tail fold and ribs.

The size of the SHEATH of the bulls ranged on a scale of 1 to 3 and was adapted from Cardoso and Lopa (2010). A SHEATH of 1 meant that the sheath was closer to the abdominal wall; a SHEATH of 2 represented those animals whose sheath depth was average; and a SHEATH of 3 was indicative of those bulls whose foreskin was not smaller than an imaginary line between the knee and the hock of the animal.

Other information such as weight at the sale, age, and scrotal circumference (SC) were collected from the sales catalogs, as well as information sheets displayed in the holding pens.

Information on the name of the auctions (auctions A to M) and number of editions, marketing strategies used to advertise the event, name of the sellers, payment conditions (at sight or in installments), post-sale warranty, media broadcasting (TV/Internet), bank credit, and possibility of free delivery were all collected from the sales catalogues or when announced by the auctioneer.

Data regarding the entry order (ORDER, i.e., the order in which bulls are presented for sale at the auction), time spent in the ring, final sale price (multiplication of the final bid price by the number of installments), buyer’s name, and destination of the bull (municipality and state of the buyer’s farm) were collected during the auction.

As for a limitation of this study, while data from Braford bulls were collected between 2013 and 2015, those for Brangus took place between 2014 and 2017. Therefore, it is likely that different economic events might have affected the prices analyzed for the distinct periods, which would end up distorting the results. Consequently, a joint analysis of the two breeds was not possible as it would distort the formation of quantiles. Thus, the prices for Braford and Brangus were analyzed separately.

2.1. Braford

Data were collected from 1,540 Braford bulls sold in 13 livestock auctions (auction A to M) held in eight municipalities in the state of Rio Grande do Sul, Brazil, in 2013, 2014, and 2015. All 13 sales were traditional livestock auctions in the state; therefore, they are well-established annual events. After data collection, collating, and analysis, 465 observations were deleted due to missing information, for example, in situations where information about the animal’s weight, date of birth, scrotal circumference, among others, was not available. Thus, a total of 1,075 observations were used.

Subsequently, independent variables were established (Table 1). The dependent variable used was individual price (US$). All nominal prices were recorded in the Brazilian currency (Real, R$), which was deflated according to the Brazilian General Price Index (IGP) as of November 2015, which was the date of the last livestock auction included in the sample. The objective of this analysis was to verify the effect of phenotypic characteristics and market factors on the selling price of Braford bulls.

2.2. Brangus

Data were collected from 1,179 Brangus bulls sold in three auctions (A, B, and C), which were held between 2014 and 2017 (Table 1), in three municipalities in the state of Rio Grande do Sul, Brazil.

=== pág. PDF 5 | rótulo - ===

Similar to the assessment of Braford, after processing the collected data, 1,082 observations remained due to some flaws in the collection of the variables, for example, in situations where information about the animal’s weight, date of birth, scrotal circumference, among others, was not available. All nominal prices were recorded in Brazilian currency and deflated according to the IGP for November 2017, which is the date of the last auction included in the sample.

In addition to the relationship between phenotypic characteristics and auction market characteristics, the genotypic characteristics of the Brangus bulls were evaluated. The genetic information could be easily accessed by catalogs (according to availability in each auction). The expected progeny difference for birth weight (EPDBW, in kg) was assessed in auctions A and B, and for weight gain from birth to weaning (EPDBTW, in kg) was evaluated in auction B, and the selection indexes for weaning (IWean) and final (IFinal) were evaluated in auction A (Table 1). In auction C, no genetic variables were evaluated. Data were from 2016 and 2017, and as in previous auctions, this information was not made available by the sellers.

The year 2014 was considered the base year, because according to the cattle price cycle, it was characterized as a scenario without significant fluctuations in the commercialization prices of beef cattle categories (NESPro, 2015). Regarding the auctions, it was stipulated that B was the base auction since it has been on the bull market for roughly 20 years and has an exclusive auction for the sale of Brangus bulls. Auction A, on the other hand, has been on the market for more than 50 years, and a single seller offers Brangus and other breeds. Lastly, auction C has been on the market for around 15 years and offers Angus and Brangus bulls from several sellers.

2.3. Statistical analyses

The prices were converted into US dollars according to the average exchange rate for that same month (the Brazilian Central Bank published information). Microsoft Excel® was used to perform the descriptive analysis.

A preliminary analysis of the normality of the data identified kurtosis; therefore, a logarithmic transformation was used to reduce the positive skewness of the high values influencing the prices. Logarithmic transformation was used to estimate the models for all variables, except for binary variables. Farrar-Glaubar test was used to detect the presence of multicollinearity.

Koenker and Bassett (1978) highlighted that QR allowed an estimation of a conditional quantile, in which each quantile represented a typical behavior of one characteristic in the conditional distribution. The authors also proposed that the QR allowed the estimation of the linear relationship between regressors of a specific quantile regarding the dependent variable (price). Therefore, QR is justified by the greater price amplitude of the sample as a result of the sale of the bull.

Model QR: Y = β0i (τ) + β1i (τ) X1 + β2i (τ) X2 + ... + βki (τ) Xk + ei (τ),

in which Y is the dependent variable (price), β0i (τ) is the regression constant, βi (τ) is the regression coefficient, ei (τ) is the independent random error, X is the independent variable, and τ is the quantile used [0,1].

The estimated coefficients and respective signals (positive or negative) were analyzed from the independent variables of the QR models. To better explain the behavior of the independent variables selected against the dependent variable (prices of bulls), five quantiles (10th, 25th, 50th, 75th, and 90th) were established, according to a study by Bekkerman et al. (2013). From the estimated coefficient values of the QR at each quantile, a degree of likely impact of the variables on the dependent variable price was established. The values of the coefficients estimated by the QR are as follows: between 0 to 0.2 = very low; 0.201 to 0.400 = low; 0.401 to 0.600 = average; 0.601 to 0.800 = high; and 0.801 to 1.00 = very high.

=== pág. PDF 6 | rótulo - ===

The software EViews® (version 9.5) was used to measure the adjusted pseudo-R2, and evaluate the likelihood test. The coefficients of the model variables were analyzed, and the analysis considered the significance levels of P<0.10, P<0.05, and P<0.01.

3. Results

3.1. Braford

A descriptive statistical analysis of the prices (normal and log) was carried out and indicated that prices presented a positive asymmetric distribution, that is, there was a greater tendency for positive deviation in relation to the mean value (Table 2). Moreover, the kurtosis indicated (Figure 1) that

Table 2 - Summary statistics of Braford bulls in auctions in Brazil

Variable Mean Median Maximum Minimum SD Kurtosis Skewness

Bull sale price (dollars) 2,945.20 2,718.37 12,838.57 1,709.94 951.77 18.83 2.58

Log bull sale price 7.94 7.90 9.46 7.44 0.27 4.09 0.72

Age (months) 29.77 25.88 47.92 21.74 5.85 - -

Scrotal circumference (cm) 39.01 39.00 49.00 31.00 2.70 - -

Weight (kg) 730.46 718.00 1190.00 465.00 99.90 - -

Frame score1 2.07 2.00 3.00 1.00 0.60 - -

Muscularity score2 2.09 2.00 3.00 1.00 0.50 - -

Body condition score3 3.91 4.00 5.00 2.00 0.54 - -

Sheath score4 1.83 2.00 3.00 1.00 0.67 - -

Ring time (seconds) 96.59 82.00 453.00 9.00 63.39 - -

Observations 1,075 - - - - - -

SD - standard deviation. 1	 Frame score: 1 = smaller to 3 = larger. 2	 Muscularity score: 1 = poorest to 3 = best. 3	 Body condition score: 1 = poorest to 5 = best. 4	 Sheath score: 1 = smaller to 3 = bigger.

14

12

10

8

Percent

6

4

2

0

6.8 7.2 7.6 8.0 8.4 8.8 9.2 9.6 10.0 10.4 10.8

Log bull sale price

Figure 1 - Histogram and Fitted Kernel Density of log Braford bulls sale prices.

=== pág. PDF 7 | rótulo - ===

the distribution was characteristically leptokurtic (kurtosis > 3), with a tendency of values falling away from the mean price value. The QR analysis estimates a linear relationship for each analyzed quantile. The estimated coefficients represent the expected shift in the location of each quantile in the conditional price distribution (Bekkerman et al., 2013). It was also possible to estimate the degree of impact generated by the variables in relation to quantiles using the QR, which enables the recording of those characteristics that influence the 10th and 25th quantiles (smaller prices), the 50th quantile (average prices), and the 75th and 90th quantiles (greatest prices).

The age of bulls acted negatively on prices in all quantiles (P<0.01), having a very low impact on price in the 25th quantile, low in the 10th and 50th quantiles, and average in the 75th and 90th quantiles (Table 3). Scrotal circumference had a positive impact on the price of the bulls (P<0.01) in all quantiles, and its degree of impact was low for the 10th and 90th quantiles and average for the remaining quantiles (25th, 50th, and 75th).

Table 3 - Estimated parameters of the log determinants for the sale price of Braford bulls in livestock auctions in

Rio Grande do Sul State, Brazil

Estimated conditional quantile

Variable

10th 25th 50th 75th 90th

Intercept 1.993** 1.914** 1.484** 2.413*** 2.765**

(2.52) (2.53) (1.90) (3.13) (2.18)

Physical characteristics

Age (months) −0.227*** −0.139** −0.263*** −0.412*** −0.401***

(−3.14) (−2.29) (−4.23) (−5.86) (−5.68)

Scrotal circumference (cm) 0.300** 0.504*** 0.484*** 0.419*** 0.375***

(2.05) (4.48) (4.83) (3.57) (2.64)

Weight (kg) 0.802*** 0.660*** 0.818*** 0.809*** 0.776***

(7.08) (5.92) (7.07) (5.83) (4.66)

Frame score1 −0.022 −0.057*** −0.025 −0.015 −0.012

(−0.75) (−2.59) (−1.12) (−0.66) (−0.48)

Body condition score2 0.062 0.140*** 0.164*** 0.138** 0.134

(1.16) (2.93) (3.14) (2.26) (1.44)

Muscularity score3 0.071** 0.070*** 0.062** 0.072*** 0.046

(2.11) (2.71) (2.32) (2.60) (0.85)

Sheath score4 −0.007 −0.004 −0.020 −0.040** −0.042

(−0.34) (−0.31) (−1.33) (−2.15) (−1.36)

Polled (“Yes”) 0.065*** 0.059*** 0.045*** 0.057*** 0.038

(2.71) (3.24) (2.99) (3.03) (1.46)

Pseudo-R2 0.34 0.37 0.41 0.40 0.41

Quasi-LR statistic 509.29 853.67 1090.10 949.36 704.48

*, **, and *** indicate statistical significance at *P<0.10, **P<0.05, and ***P<0.01; t-values are in parentheses. 1	 Frame score: 1 = smaller to 3 = larger. 2	 Body condition score: 1 = poorest to 5 = best. 3	 Muscularity score: 1 = poorest to 3 = best. 4	 Sheath score: 1 = smaller to 3 = bigger.

=== pág. PDF 8 | rótulo - ===

The weight of the bulls positively influenced their prices (P<0.01), mainly in the 25th quantile. The frame of the bulls negatively influenced the price, attracting low values (25th quantile; P<0.01). This means that the buyers discount the prices for each unit of increase of FRAME. Nonetheless, MUSC positively influenced prices in the 10th, 50th (P<0.01), 25th, and 75th (P<0.05) quantiles. The BCS also positively influenced prices in the 25th, 50th (P<0.01), and 75th (P<0.05) quantiles. The SHEATH negatively influenced the prices of bulls in the 75th quantile (P<0.05); there was a discount of approximately 3% in the price of bulls from the 75th quantile for every 1 score higher. The variable POLLED positively affected the prices in all quantiles (P<0.01), except for the 90th quantile. Despite FRAME, MUSC, BCS, SHEATH, and POLLED having positively influenced prices in several quantiles, the degree of influence was very low on the final price paid.

In relation to the base year, 2014 had a positive impact on the price of bulls from the 25th to the 90th quantiles (P<0.01), and 2015 influenced the prices paid in all quantiles (P<0.01). This means that bulls sold in 2014 and 2015 were more expensive than bulls sold in 2013 (Tables 4 and 5).

Table 4 - Estimated parameters of the year, entry order and ring time of the log determinants for the sale price

of Braford bulls in livestock auctions in Rio Grande do Sul State, Brazil

Estimated conditional quantile

Variable

10th 25th 50th 75th 90th

Intercept 1.993** 1.914** 1.484** 2.413*** 2.765**

(2.52) (2.53) (1.90) (3.13) (2.18)

Marketing factors

Year 2014 0.075 0.044* 0.184*** 0.182*** 0.151***

(1.32) (2.87) (7.12) (5.08) (2.80)

Year 2015 0.173*** 0.051*** 0.290*** 0.294*** 0.258***

(2.79) (4.70) (10.88) (7.31) (4.30)

Entry order −0.069*** −0.078*** −0.096*** −0.121*** −0.140***

(−5.24) (−6.66) (−5.97) (−5.86) (−4.07)

Ring time (seconds) −0.018 −0.026** −0.011 0.013 0.048***

(−1.17) (−2.14) (−1.03) (0.86) (2.72)

Pseudo-R2 0.34 0.37 0.41 0.40 0.41

Quasi-LR statistic 509.29 853.67 1090.10 949.36 704.48

*, **, and *** indicate statistical significance at *P<0.10, **P<0.05, and ***P<0.01; t-values are in parentheses.

The ORDER showed a negative effect on the prices in all quantiles (P<0.01), meaning there was a decrease in the price during the progress of the auction. The ring time was another characteristic that negatively impacted the prices paid, particularly in the 25th quantile (P<0.05), but positively affected prices in the 90th quantile (P<0.01; Table 4).

The variable auction was an indicator of the effect of the different locations where auctions took place (Table 6). The auction used as the baseline is traditional and has occurred since 2003 (auction B). In this auction, the commercialized bulls are only from two sellers, and the Internet is used as a sales channel offering an 8% discount for payment in cash.

=== pág. PDF 9 | rótulo - ===

Table 5 - Estimated parameters of auctions of the log determinants for the sale price of Braford bulls in livestock

auctions in Rio Grande do Sul State, Brazil

Quantile regression: estimated conditional quantile

Variable

10th 25th 50th 75th 90th

Intercept 1.993** 1.914** 1.484** 2.413*** 2.765**

(2.52) (2.53) (1.90) (3.13) (2.18)

Marketing factors

Auction

A 0.059 0.020 −0.076 −0.174*** −0.178**

(0.78) (0.29) (−0.93) (−2.63) (−2.15)

B 0.068 0.058 −0.035 −0.090 −0.076

(1.45) (0.22) (−0.50) (−1.41) (−0.84)

C 0.159* 0.199*** 0.123 0.078 0.102

(1.94) (3.02) (1.62) (1.26) (1.22)

D −0.043 −0.023 −0.128* −0.138** −0.100

(−0.78) (−0.43) (−1.71) (−2.13) (−1.04)

E −0.006 −0.025 −0.119 −0.112 0.002

(−0.16) (−0.52) (−1.59) (−1.44) (0.02)

F 0.133* 0.237*** 0.168** 0.078 0.098

(1.99) (3.62) (2.18) (1.25) (1.47)

G 0.135*** 0.073 −0.081 −0.138* −0.052

(2.84) (1.61) (−1.08) (−1.92) (−0.57)

H 0.061 0.039 −0.120* −0.228*** −0.211***

(1.16) (0.82) (−1.66) (−3.56) (−2.74)

I 0.109** 0.085* −0.048 −0.174*** −0.146*

(2.26) (1.76) (−0.67) (−2.82) (−1.55)

J 0.122** 0.068 −0.036 0.039 0.147

(2.48) (1.42) (−0.44) (0.44) (1.24)

K 0.029 −0.002 −0.097 −0.186*** −0.119

(0.48) (−0.03) (−1.27) (−2.85) (−1.12)

L 0.337*** 0.306*** 0.171** 0.054 0.075

(7.91) (6.58) (2.36) (0.89) (0.88)

Pseudo-R2 0.34 0.37 0.41 0.40 0.41

Quasi-LR statistics 509.29 853.67 1090.10 949.36 704.48

*, **, and *** indicate statistical significance at *P<0.10, **P<0.05, and ***P<0.01; t-values are in parentheses.

3.2. Brangus

The prices of Brangus bulls sold at auctions show considerable variation in prices, which is characteristic of this market in Brazil (Table 7).

Weight and SC positively affected the Brangus sales price for all quantiles (P<0.01; Table 8). The age of animals at the time of auction had a negative influence on the prices of bulls in the 75th and 90th

quantiles (P<0.01), that is, bulls with the highest prices had discounts from 17 to 27% in prices for each additional month of life they had in the 75th and 90th quantiles, respectively.

The FRAME had a positive influence on the prices of the 10th quantile (P<0.10) and a negative influence on the prices of the 75th quantile (P<0.05). The BCS positively influenced the prices in the 10th (P<0.05) and 75th (P<0.01) quantiles, indicating that there are different interests on the part of the

=== pág. PDF 10 | rótulo - ===

Table 6 - Characteristics of the livestock auctions for Braford bulls in Rio Grande do Sul State, Brazil

Auction Editions Seller Broadcasting Warranty Discount payment (%) Delivery

A 9 2 - Yes - -

B - 2 Internet - 8 Yes

C 51 1 Internet Yes 10 Yes

D 13 3 Internet Yes 8 Yes

E 16 15 TV/Internet Yes 10 Yes

F 61 1 TV/Internet Yes 10 Yes

G 5 5 None No (6 to 7) No

H 15 2 - No 7 Yes

I 6 2 None No (7 to 10) Yes

J 59 5 TV - 8 -

K 12 4 TV - 8 -

L 16 1 Internet Yes 10 Yes

M1 13 2 Internet Yes 8

1	 Auction event used as base for the Dummy variable (AUCTION).

Table 7 - Descriptive statistics of Brangus bulls sold at auctions in the Rio Grande do Sul State, Brazil

Variable N Average Median Maximum Minimum SD Kurtosis Skewness

Price per bull (dollar) 1,082 3,284 3,107 7,768 1,862 1,031 4.98 1.24

Price (log) 1,082 8.05 8.04 8.95 7.52 0.29 2.86 0.41

Age (months) 1,082 27.55 24.88 50.32 21.08 5.47 - -

Scrotal circumference (cm) 1,082 39.04 39.00 51.00 30.00 3.27 - -

Weight (kg) 1,082 657.53 640 959 432 100.62 - -

Frame score (1-3) 1,082 2.10 2 3 1 0.58 - -

Muscularity score (1-3) 1,082 2.16 2 3 1 0.52 - -

Body condition score (1-5) 1,082 4.21 4 5 2 0.44 - -

Sheath score (1-3) 1,082 1.87 2 3 1 0.70 - -

EPDBW (kg) 450 0.074 0.02 1.8 −1.5 0.48 - -

EPDBTW (kg) 197 −0.20 −0.40 9.5 −5.5 2.99 - -

IWean 250 10.05 10.4 36.1 −11.20 7.9 - -

IFinal 250 9.93 9.5 30.4 −4.8 6.39 - -

EPDBW - expected progeny difference for birth weight; EPDBTW - expected progeny difference for weight gain from birth to weaning; IWean weaning index; IFinal - final index; SD - standard deviation.

buyers regarding the visual characteristics of bulls. According to the results, only in the 75th quantile (P<0.05) did the SHEATH have a negative effect on price, that is, with each increase in the score, the price of bulls decreases in this quantile.

The behavior of bull buyers according to the year is partly associated with the price of the other buying categories (steer and calf), and the results of bull price scenarios between 2014 and 2017 confirmed this statement. With regard to the year variable, 2015 positively influenced prices in the 50th (P<0.05), 75th (P<0.01), and 90th (P<0.05) quantiles; that is, animals that are sold at intermediate to high prices received an increase in price in relation to those sold in 2014 (Figure 2). Bulls sold in 2017, on the other hand, had a decrease in prices compared with the 2014 price scenario for all quantiles (P<0.01), except the 90th.

=== pág. PDF 11 | rótulo - ===

Table 8 - Estimated parameters of the price determinants of Brangus bulls in auctions held in the Rio Grande do Sul

State, Brazil

Estimated quantile

Variable

10th 25th 50th 75th 90th

Intercept 2.419*** 1.737*** 1.482*** 0.418 −1.261**

(3.93) (3.38) (3.33) (0.98) (−2.07)

Physical characteristics

Age (months) −0.045 −0.082 −0.084 −0.173*** −0.270***

(−0.37) (−0.89) (−1.25) (−3.06) (−4.03)

Scrotal circumference (cm) 0.233** 0.314*** 0.342*** 0.329*** 0.541***

(2.00) (3.13) (3.76) (4.07) (2.82)

Weight (kg) 0.673*** 0.793*** 0.826*** 1.00*** 1.20***

(4.39) (6.75) (8.39) (11.18) (9.7)

Frame score (1-3) 0.068* 0.031 0.003 −0.039** −0.004

(1.88) (1.20) (0.17) (−2.14) (−0.16)

Body condition score (1-5) 0.175** 0.054 0.085 0.213*** 0.149

(2.13) (0.61) (1.36) (2.99) (1.13)

Muscularity score (1-3) 0.009 0.015 0.005 −0.001 0.013

(0.20) (0.45) (0.21) (−0.05) (0.41)

Sheath score (1-3) −0.024 −0.023 −0.018 −0.03** −0.037

(−1.43) (−1.48) (−1.21) (−2.26) (−0.96)

Marketing factors

Year 2015 0.026 −0.015 0.051** 0.088*** 0.116**

(−0.93) (−0.60) (2.79) (4.32) (2.47)

Year 2016 −0.006 0.018 0.013 −0.006 −0.013

(−0.02) (0.90) (0.82) (−0.36) (−0.46)

Year 2017 −0.09*** −0.10*** −0.11*** −0.096*** −0.056

(−4.55) (−5.34) (−7.26) (−5.16) (−1.45)

Auction A 0.264*** 0.282*** 0.316*** 0.320*** 0.264***

(13.4) (14.6) (18.2) (18.25) (7.44)

Auction C −0.086** −0.054 −0.017 0.001 −0.047

(−2.07) (−1.76) (−0.70) (0.07) (−1.13)

Pseudo-R2 0.39 0.40 0.43 0.40 0.41

Quasi-LR statistic 601.62 859.30 1239.2 1133.6 600.35

Pseudo-R2 is used for quantile regression. *, **, and *** indicate statistical difference at *P<0.10, **P<0.05, and ***P<0.01; t-values are in parentheses.

The place of sale is one of the factors that can influence the price of bulls, and we found that auction A positively influenced the price of Brangus bulls in all quantiles (P<0.01) when compared with the base auction B. Auction C suffered a price penalty only on bulls sold at lower prices (10th quantile; P<0.05), when compared with bulls sold in this price range at auction B.

There was little effect of genotypic characteristics on the different selling prices of bulls at the auctions (Table 9). The EPDBW and EPDBTW did not interfere with bull prices. For the analyzed indices, it was found that IWean had a positive influence on the 90th quantile only (P<0.10), and IFinal was found to have a positive influence on the 50th (P<0.10) and 75th (P<0.05) quantiles.

=== pág. PDF 12 | rótulo - ===

Year 2015 2016 2017

0.15

**

0.1

***

**

0.05

*** ***

*** ***

0

-0.05

Model coeficient

-0.1

10th 25th 90th 75th 50th

-0.15

Quantiles

The negative model coefficient indicates that the selling prices of bulls in each year (2015, 2016, 2017) were lower than in the year 2014. The positive model coefficient indicates that the selling prices of bulls in each year (2015, 2016, 2017) were higher than the prices of bulls traded in 2014. ** and *** indicate statistical difference at **P<0.05 and ***P<0.01.

Figure 2 - Price behavior of Brangus bulls in auctions according to the year of sale (2015, 2016, and 2017) in

the established quantiles (10th, 25th, 50th, 75th, and 90th) (base year: 2014).

Table 9 - Genotypic parameters and selling price of Brangus bulls sold at auctions in the Rio Grande do Sul

State, Brazil

Estimated conditional quantile

Variable

10th 25th 50th 75th 90th

EPDBW (kg) −0.019 −0.031 −0.001 −0.007 0.013

(−0.54) (−1.44) (−0.12) (−0.45) (0.59)

Pseudo-R2 0.50 0.51 0.49 0.44 0.42

EPDBTW (kg) 0.004 0.011 0.006 0.006 0.002

(0.77) (2.55) (1.21) (0.78) (0.15)

Pseudo-R2 0.30 0.41 0.43 0.46 0.48

IWean 0.0008 0.001 −0.0003 0.0002 0.004*

(0.30) (0.54) (−0.14) (0.12) (1.7)

IFinal 0.003 0.002 0.005* 0.008** 0.006

(0.76) (1.19) (1.90) (2.54) (1.35)

Pseudo-R2 0.23 0.17 0.24 0.31 0.34

EPDBW - expected progeny difference for birth weight; EPDBTW - expected progeny difference for weight gain from birth to weaning; IWean weaning index; IFinal - final index. Pseudo-R2 is used for quantile regression. * and ** indicate statistical difference at *P<0.10 and **P<0.05; t-values are in parentheses.

4. Discussion

The study was comprised of two analyses carried out at different times. The Braford analysis was carried out between 2013 and 2015, and the Brangus analysis was carried out between 2014 and 2017, both breeds sold in traditional auctions located in Rio Grande do Sul State, Brazil. This discussion will address the two analyses jointly whenever possible, as they are synthetic breeds that have a similar interest on the part of producers.

=== pág. PDF 13 | rótulo - ===

The prices of Braford and Brangus bulls tend to disperse away from the mean value and become leptokurtic. Thus, QR enables a better understanding of the factors influencing the inferior and superior tails of the conditional price distribution. The price depends on the timing of each auction and the willingness of buyers to pay more or less for the animals as a result of their preferences, and these factors may vary according to the genetic makeup of their livestock, objectives, and other characteristics of the production system (Holt et al., 2004).

4.1. Phenotypic characteristics

Age negatively affected all quantiles of Braford (very low impact in the 25th quantile; low impact in the 10th and 50th quantiles; and average impact in the 75th and 90th quantiles) and Brangus (75th and 90th quantiles) bulls; however, it affected more bulls that attracted a greater value, which were in the 75th and 90th quantiles.

Age can have an impact on the economic return of the activity, which is usually higher when producers acquire younger animals, as they stay longer in the herd. Consequently, bull buyers who pay more tend to penalize the price of animals for every month of life, that is, they buy expensive, but young bulls. In research conducted by Irsik et al. (2008), bulls of different breeds that had an average age of approximately 26 months, similar to that of the present study, also had a discount in their price for every additional month of life. This supports the notion that buyers of synthetic bull breeds prefer younger animals. One probable explanation is that in the auctions, the biggest offer is normally made for young bulls (two years of age) and another may be due to the fact that these bulls have more longevity in the herd compared with older bulls. Not only longevity, but younger bulls have newer genetics, and by buying younger bulls, the operations are trying to have what is the latest in terms of genetics. The most common age for bull commercialization is two years of age. Bulls older than 25 months were less attractive in Brazilian auctions, probably because these animals were not sold during the year (and were three years of age) or because of the low market demand.

In the United States of America (USA), bulls are typically sold at one year of age or older (Chvosta et al., 2001). In Brazil, they are sold later (at two years of age) when compared with animals marketed in the USA, and this is due to the extensive cattle production systems found in Brazil. Chvosta et al. (2001) proposed that buyers prefer older bulls because they are more reproductively efficient.

Within the quantiles analyzed for synthetic bull breeds, it could be observed that with an increase in SC, the price paid for the animals in all quantiles increased. Buyers pay a lot of attention to SC, mainly because it is easy to identify and interpret the data provided through catalogs. In auctions in Brazil, SC evaluation generally occurs prior to the event and, therefore, there could be confusion between the effects of genetics and those caused by the environment. For example, the supercharging provided to the bull during preparation for the auction may hide a small SC, in which case the SC would not be correlated with the genotype, but to the weight of the bulls in preparation for the auction. This would lead to buyers misinterpreting the SC and the potential fertility of the bulls (Parkinson, 2004). Scrotal circumference is usually considered a good reproductive characteristic and, when selecting it, farmers are able to quickly improve the herd’s fertility and genetics (Bourdon and Brinks, 1986). The buyers’ overprice valuation of animals with a greater SC may have other positive aspects, as this has a positive genetic correlation with body weight of yearling (Frizzas et al., 2009; Ríos-Utrera et al., 2018) and weaning animals (Eler et al., 1996; Cyrillo et al., 2001), which indicates that information about SC may be one of the major factors influencing the selection of bulls.

Buyers put emphasis on the weight of the animal at the time of sale, regardless of the sales price. Normally, heavy animals are related to a good visual appearance and are considered to be of superior quality. According to Commer Jr. et al. (1990), visual cues are important factors in the selection and purchase of cattle. When estimating prices of bulls in Canada, Walburger (2002) also noted that there was a positive correlation between the weight of a bull and the price. However, excessively heavy animals might have difficulty in natural pastures, as excess weight causes problems in their joints (Menegassi and Barcellos, 2015), which could increase the risk of injuries. Another factor that should

=== pág. PDF 14 | rótulo - ===

be considered when buying heavier bulls is the size of the females that will be paired with these bulls, since light females mated with heavy bulls have a higher risk of hip and hindlimb injuries.

In Brazilian auctions, the auctioneer usually places emphasis on SC and weight at the time of sale, which may also influence the price of bulls (from the 10th to 90th quantile). This can be associated with the concern of buyers to acquire animals that can contribute to a greater weight gain of the progeny. However, the preference of buyers should be for animals with a weight appropriate to their body size when used for field mating.

There was a distinct influence of the FRAME on the selling price of bulls. At the lowest prices (10th

quantile) of sales of Brangus bulls, this influence was positive, and in the highest prices (75th quantile), it was negative. In Braford bulls, the frame size had a negative effect on bulls that received low prices (25th quantile), with a price decrease, and this can be linked to the profile of buyers. Buyers of high-priced Brangus bulls prefer smaller framed bulls, possibly because of the lower maintenance costs of this animal (Şentürklü et al., 2021). This may be appropriate under breeding conditions in Brazil, because the production system is based on natural pastures, and it is important to acquire a bull with a frame suitable for the production system used (Smith, 2014).

The profile of buyers favoring smaller animals could be attributed to the fact that they might not need large animals in their herds. In addition, the larger the bull frame, the greater the maintenance nutrient requirements (NRC, 1996). On the other hand, a bull with a smaller structure can make the size of the adult cow in the herd also smaller in subsequent generations. This is the opposite of what Atkinson et al. (2010) observed in their study on cow-calf systems in the USA. They found that FRAME had a positive impact on the price of different breeds and concluded that American farmers would prefer animals with moderate to large frame because they expect prices to be higher.

The ideal size of a bull to be used in the herd is still a difficult decision for buyers, especially in Brazil with different production systems. Using larger bulls for breeding, the tendency is to wean larger calves, which would be positive for the calf sellers, as buyers tend to look for larger animals (Christofari et al., 2008), also leading to a possible profit from the production of larger cattle. This could lead to a possible increase in production costs, since larger animals demand more feed (Bir et al., 2018) and in this sense, the purchase of animals with a smaller frame could minimize production costs.

In most cow-calf production systems, reproductive management occurs through natural mating, which produces high energy expenditure by the bull. Therefore, there is a decrease of one to two units of the BCS of bulls during the mating season (Menegassi and Barcellos, 2015). This justifies the results of our work that demonstrates higher prices are paid for bulls with a higher BCS. The BCS had a positive influence on prices, particularly for those in the 50th quantile for Braford bulls and in the 10th and 75th quantiles for Brangus bulls. This result indicates that bulls with a greater BCS tend to be more valued by producers; however, not all buyers value bulls by their BCS. The likely explanation for this may be related to the proposed use of this bull, for natural mating. A BCS of 4 would be an ideal type of body condition for use in natural pasture systems (Menegassi and Barcellos, 2015), because the animals have a good muscular score and proper body energy reserve, which will be mobilized in the mating season.

As for muscularity, there was an increase in the price of bulls, in which MUSC was significant from the 10th to the 75th quantile, in Braford bulls only. Usually, buyers prefer such a characteristic because they expect it to be transmitted to the progeny and because it is related to the production of heavier carcasses (Bouquet et al., 2010). Dhuyvetter et al. (1996) also found a positive effect of MUSC on the prices of bulls.

The Braford is a cross between the Hereford × Brahman or Hereford × Zebu breeds, and the Brangus is a cross between the Brahman × Angus or Angus × Zebu breeds. Due to the presence of Brahman and Zebu breeds in these crossings, synthetic bull breeds may have developed undesirable foreskin that are included in the selection criteria of buyers. The size of the foreskin is an important characteristic, as its size and shape can negatively interfere with the mating behavior of a bull,

=== pág. PDF 15 | rótulo - ===

or by increasing the probability of foreskin injury caused by tropical pastures in Brazil (Torres Júnior et al., 2003). The influence of the SHEATH has been noted in bulls of greater value (75th quantile) because they attracted a price reduction for each increase in the foreskin score. Excess skin on the foreskin can present reproductive and health problems, and insufficient skin represents a lack of breed character, so it is desirable for the bull to have an intermediate size foreskin, without excess skin (Kriese et al., 1991).

It is likely that bulls sold in the 75th quantile were filling the seedstock cattle market demand, whose companies look for bulls with smaller SHEATH. Seedstock cattle are considered genetic suppliers by providing semen from bulls that enable genetic improvement; however, in Brazil, the improvement in cattle herds is mostly conducted through natural mating. The emphasis placed on this variable by buyers of synthetic bull breeds has not yet been studied in previous research on the marketing of breeders.

The presence or absence of horns in Braford bulls is related to the Hereford (with horns or polled) × Zebu cross. The POLLED characteristic tended to positively influence prices, particularly in the 10th and 75th quantiles. Dhuyvetter et al. (1996) mentioned that polled animals were preferable to those with horns, which tended to attract 10% more in price because polled bulls are easier to manage. Therefore, buyers should give preference to polled animals, since the absence of horns reduces the risk of injuries to humans and other animals in the herd, requires less feeding-trough space, and decreases the incidence of carcass wastage due to bruising (Stock et al., 2013).

In general, buyers of synthetic bull breeds at auctions emphasize the phenotypic characteristics, that is, the visual appeal is a decisive factor in decision-making when purchasing bulls (Commer Jr. et al., 1990). Visual assessment is important for assessment of balance, structural aspects, angulation, and temperament, among other features (Holt et al., 2004). The responses obtained in the quantiles must be interpreted carefully, as the emphasis given to the characteristics mentioned above can depreciate a bull with a good breeding potential that does not have a good physical appearance (Chvosta, 1997). The selection of bulls must combine visual aspects and genetic performance to make more appropriate decisions in the selection of breeders (Holt et al., 2004).

4.2. Genotypic characteristics

Genetic information of the bulls is made available at auctions through sales catalogs, aiming at helping buyers to choose a bull. The catalog data for the genetic information differed between auctions, due the index of interest for each auction. This seems to be related to the interest of the seller in presenting the data related to EPD and selection indexes of the bulls, which did not allow for a joint analysis of the data of all the auctions evaluated. As for the number of observations used for genetic data, it is common for research to use data from several breeds of bulls in the same study (Dhuyvetter et al., 1996; Chvosta et al., 2001), which results in a reduction in the amount of genetic data for each breed (Atkinson et al., 2010; Brimlow and Doyle, 2014).

The evaluation of genetic data when buying a bull allows buyers to acquire breeders that will implement genetic gains in the herd through their selection of bulls. In this study, the EPDBW had no effect on the prices of Brangus bulls. Buyers should observe the EPDBW of bulls, as it is the best indicator of the expected weight at calf birth (Parish and Rhinehart, 2008). However, when we observe an average EPDBW (0.07 in this study) close to zero, there is an indication that bulls may not generate dystocia in cows, especially in young females. Most surveys mentioned that bulls with higher EPDBW values tend to be sold at lower prices than bulls with lower EPDBW (Dhuyvetter et al., 1996; Jones et al., 2008; Chvosta, 1997).

The EPDBTW did not influence the prices of Brangus bulls. The initial phase of life of the animal until weaning represents a period of accelerated growth and development, and the selection of animals with positive EPD would be the most appropriate (Magnabosco et al., 2013); however, according to the data, the average EPDBTW of the evaluated bulls is negative; thus, the tendency is that the Brangus

=== pág. PDF 16 | rótulo - ===

bulls evaluated will not have progeny heavier at weaning compared with those with positive DEPBTW. However, high EPDBTW requires high nutritional levels to meet the energy demand for animals with high growth potential from birth to weaning, so they are recommended for systems with good availability and quality of forage.

The IWean influenced the prices of Brangus bulls (90th quantile). It reflects the total genetic merit of the animal, formed by the combination of the weight gain, conformation, precocity, and musculature during weaning. Most commercial producers sell calves per kilogram of body weight, that is, the producer seeks to make a greater quantity of product available on the market (Chvosta et al., 2001; Vestal et al., 2013), and consequently, a higher remuneration with the sale of heavy calves.

The IFinal represents the total genetic merit of the animal in a single value, calculated in percentage weightings of the weaning and yearling EPD. The IFinal had a positive influence on bull prices (50th and 75th quantiles). In this sense, buyers realized that this index may indicate a bull that is more likely to gain weight in the year and valued bulls based on this characteristic. According to research by Magnabosco et al. (2013), who evaluated Nellore bulls, yearling weight showed moderate heritability, thus, this characteristic tends to be transmitted to the progeny, providing gains for future generations.

It was found that the results of the genetic data in this study had little influence on the prices of Brangus bulls (EPDBW, EPDBTW, IWean, and IFinal), which may be related to buyers not valuing genetic factors when purchasing bulls at auctions (Chvosta, 1997), due to a lack of knowledge or lack of confidence in the data, among other reasons. However, this does not imply that genetic factors have no value. It should be noted that the use of genetic information available in catalogs is a useful tool for choosing bulls, using more objective criteria when compared with using only the phenotypic characteristics; however, there are some possible explanations for the limited emphasis given to genetic criteria in auctions in Brazil. The approach to EPD and indexes in catalogs is confusing and may not provide complete and adequate information, in addition to not allowing comparison of the genetic data of bulls in the same auction by buyers. For example, the EPDBW and EPDBTW variables that must be analyzed at the time of purchase were not available for analysis in around 50% of the bulls sold.

The availability of genetic data for bull buyers was reported in research by Jones et al. (2008). They found that although the American Association of Angus encourages sellers to provide as much information as possible to buyers, even within the same breed there is no a pattern in the data presented in the catalogs. Similar to what occurs in the sale of bulls of synthetic breeds in auctions in Brazil, there is information on different EPD among the bulls sold, not allowing an equivalent comparison between them. Moreover, with the possible lack of knowledge of buyers on the goals of genetic data, it diminishes the importance of these data when choosing a bull. Thus, producers prefer to use criteria that can be easily viewed and is widely understood, such as body weight and SC.

4.3. Marketing factors

The ORDER of the Braford bulls sale negatively influenced the prices paid, with an increase in the discount observed over the auction. It could be said that the ORDER influences the different prices of the bulls, that is, those animals that are shown at a later ORDER are devalued. In addition, there was an increase in price discount. This fact is supported by previous research conducted by Dhuyvetter et al. (1996) and Jones et al. (2008), who found that the price of bulls decreased as sales progressed due to a lack of interest and a smaller pool of buyers. The price reduction that occurred during the auctions can also be explained by the quality of the animal (Evangelista et al., 2019) and buyer behavior. Sellers tend to offer the best quality animals at the beginning of the auction, and buyers are willing to pay more for these animals.

The time that the Braford bulls remained in the ring negatively influenced the price of bulls in the 25th quantile, which could be related to the perceived quality of the animal. The bulls drew a discount

=== pág. PDF 17 | rótulo - ===

for every second of extra time that they stayed in the ring. In the 90th quantile, typical of bulls of greater value, the time in the ring had a positive influence on the price. This can be attributed to the characteristics of the animals, which were more enthusiastically highlighted by the auctioneers, as well as rivalry between buyers, who increased the number of bids and extended the time the bulls stayed in the ring.

The economic situation of the beef sector at the time of the auction, as well as the cattle price cycle, can definitively influence marketing strategies. The change in prices of bulls over the years can have several reasons, such as the cattle cycle, the price of calves and oxen for finishing, market trend in relation to the physical characteristics of the animal, global and national economy, among other factors (Irsik et al., 2008). In our study, the effect of year on sales prices was shown, and the prices between 2013 and 2015 of Braford bulls increased by 14%.

There was a tendency for valorization of Brangus bulls (of medium and high prices) sold in 2015, in relation to the base year 2014 (Figure 2). Producers who were willing to pay more for synthetic bull breeds in 2015 possibly had an interest in productivity benefits, as the cattle price cycle was on the rise, and consequently, the investment spent on buying bulls was larger. During this period, the price of ox farming in Brazil was on the rise, that is, prices were passed on to other categories, including bulls.

In 2016, only the commercialization of Brangus bulls was evaluated, and there was a reduction in the price of cattle, which was associated with several factors, including an increase in the supply of cattle, a reduction in the consumption of beef, and a drop in prices for other meats (Barcellos et al., 2019). However, the fluctuations in the prices of cattle and calves do not seem to have a great effect on the prices of bulls sold in 2016, as they remained stable in relation to 2014, and can be associated with the high demand for bulls in auctions. Even with price reductions in other categories, bull buyers still paid similar prices to those for bulls in 2014. In this period, producers may have sought ways to reduce their unit cost of production (Prevatt, 2017), and even with the tendency to reduce prices, prefer to pay for a price similar to the price practiced in 2014 as one of the possibilities to maintain or reach higher levels of profitability.

However, the cycle of cattle price reduction in Brazil remained in 2017 (NESPro, 2018), and according to the results obtained, there was a discount in practically all the different prices of bulls. As such, there was a transfer of the prices of oxen to the bull category, placing a limit on the amount that farmers were willing to pay. Between 2014 and 2017, the cattle price cycle in the USA was similar to that in Brazil, with a substantial drop in 2017 (NASS/USDA, 2018), which is related to several factors, such as consumer confidence, domestic and international beef demand, input prices, and competition with other meats (Prevatt, 2017).

Another variable associated with price behavior is the auction factor, which influences sales prices due to the different characteristics of each auction. In Braford analysis, auction A had a positive influence on the prices of bulls when compared with the base auction (B). Although auctions A and B are exclusive, meaning they only sell bulls from one seller, A has been in the bull auction market for more than 50 years, which can indicate a positive reputation for buyers, generating the impact of the seller in the formation of the price (Maxa et al., 2009).

Compared with auction B, in auction C, only bulls that received the lowest prices (10th quantile) were penalized by buyers. Auction C offers bulls from more than one seller, which increases the possibility of presenting breeders with different characteristics from a range of bulls, and the shorter time spent in the bull market may reflect a lower selling price. However, there are other factors that can influence the price of an animal at the auction, such as trust between buyers and sellers, which is difficult to measure.

At Braford auctions, it was observed that auctions C, F, and L had appreciation for bulls that were sold at lower prices when compared with the base (M). Braford bulls sold at higher prices were penalized in auctions A, H, and I, which have been on the bull market for less than 16 years. The price behavior

=== pág. PDF 18 | rótulo - ===

in these auctions can be related to the number of edits, that is, with the operation time in this type of market and possibly with the reputation of the seller. Jones et al. (2008) mentioned that the location of the event also influenced the price of Angus bulls sold in auctions in the USA.

To fill current gaps in the literature, this study attempts to evaluate the location of the auction. The locations influenced the price paid for bulls due to locality, marketing efforts, and sales conditions. We realized that many sellers have been established in the market for a long time with continuous auction events being held for over ten years. Both auctioneers and sellers engage in the promotion of events to attract more buyers. The sellers tend to offer promotional sale conditions, such as post-sale guarantees, with the purchase and the price paid for the bulls possibly influencing the type of guarantee, and a reduction in payment at sight and delivery livestock arrangements has been reported. Transportation arrangements are important for remote buyers, particularly those using the Internet or TV to make purchases. Buyers who live far away can be attracted to a specific auction event by using the Internet or TV, thus enhancing the probability of bids and disputes between buyers.

5. Conclusions

Buyers of bull of synthetic breeds in auctions of Rio Grande do Sul State, Brazil, value phenotypic characteristics such as age, weight, and scrotal circumference in detriment of other characteristics such as frame score, muscularity score, BSC, and sheath. Selecting bull for breeding systems based on phenotype factors may improve the production system in the short term; for constant gains it is also important to use genotypic characteristics as a criterion for selection. These include measurements such as the expected progeny differences and selection indexes used in this study, because the choice based on these can bring permanent genetic gains to the herd. The low importance of genetic values in sales catalogs of Brangus bulls may be related to distrust of the data or the lack of genetic information presented in catalogs. However, the selection of bulls based on genetic data, instead of just phenotypic characteristics, is the best way for productivity gains on a medium- to long-term scale in beef cattle herds.

Conflict of Interest

The authors declare no conflict of interest.

Author Contributions

Conceptualization: E.D. Sartori, S.R.O. Menegassi and R.P. Oaigen. Data curation: J.F. Lopes, M.E.A. Canozzi, M.K. Rocha, E.D. Sartori, S.R.O. Menegassi, R.P. Oaigen and D. Zago. Formal analysis: J.F. Lopes and E.D. Sartori. Funding acquisition: J.O.J. Barcellos. Investigation: J.F. Lopes, M.E.A. Canozzi, T.L. Gonçalves, M.K. Rocha, A.G. Sessim and I.P. Pereira. Methodology: J.F. Lopes, T.L. Gonçalves, A.G. Sessim, S.R.O. Menegassi and C. Koetz Junior. Project administration: J.O.J. Barcellos. Resources: J.O.J. Barcellos. Software: L.K. Aguiar. Supervision: L.K. Aguiar and J.O.J. Barcellos. Validation: M.K. Rocha and C. Koetz Junior. Visualization: T.L. Gonçalves, S.R.O. Menegassi and D. Zago. Writing – original draft: J.F. Lopes, M.E.A. Canozzi and A.G. Sessim. Writing – review & editing: L.K. Aguiar, D. Paparas, R.P. Oaigen, D. Zago and J.O.J. Barcellos.

Acknowledgments

The authors are grateful for the financial support of the Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq).

=== pág. PDF 19 | rótulo - ===

References

ABB - Associação Brasileira de Brangus. 2022. Rebanho Brangus cresce mais de 80% no Brasil em dez anos. Available at: <https://www.brangus.org.br/noticias-raca-brangus/rebanho-brangus-cresce-mais-de-80-no-brasil-emdez-anos>. Accessed on: Feb. 01, 2023.

ABHB - Associação Brasileira de Hereford e Braford. 2018. Braford. Available at: <http://www.abhb.com.br/Braford/ Braford/>. Accessed on: Apr. 25, 2018.

ABHB - Associação Brasileira de Hereford e Braford. 2023. Braford. Available at: <https://www.abhb.com.br/as-racas/ braford/>. Accessed on: Feb. 01, 2023.

Atkinson, R.; Sanders, D. R.; Jones, K. and Altman, I. J. 2010. An evaluation of purebred bull pricing: Implications for beef herd management. Journal of the ASFMRA 2010:235-243. https://doi.org/10.22004/ag.econ.96418

Barcellos, J. O. J.; Oliveira, T. E. and Lima, J. A. 2019. Conjuntura da pecuária de corte – uma análise trienal. In: Centro de Inteligência de Bovinos de Corte - Sul, NESPro and EMBRAPA (eds). Carta conjuntural 1:1-5. Available at: <https://www.ufrgs.br/nespro/wp-content/uploads/2021/04/carta-conjuntural-v1-n1-jan2019.pdf>. Accessed on: Feb. 01, 2019.

BIF - Beef Improvement Federation. 1986. Guidelines for uniform beef improvement programs. University of North Carolina, Raleigh, NC, USA.

Bekkerman, A.; Brester, G. W. and McDonald, T. J. 2013. A semiparametric approach to analyzing differentiated agricultural products. Journal of Agricultural and Applied Economics 45:79-94. https://doi.org/10.1017/S1074070800004594

Bir, C.; De Vuyst, E. A.; Rolf, M. and Lalman, D. 2018. Optimal beef cow weights in the U.S. Southern Plains. Journal of Agricultural and Resource Economics 43:103-117.

Bouquet, A.; Fouilloux, M. N.; Renand, G. and Phocas, F. 2010. Genetic parameters for growth, muscularity, feed efficiency and carcass traits of young beef bulls. Livestock Science 129:38-48. https://doi.org/10.1016/j.livsci.2009.12.010

Bourdon, R. M. and Brinks, J. S. 1986. Scrotal circumference in yearling Hereford bulls: Adjustment factors, heritabilities and genetic, environmental and phenotypic relationships with growth traits. Journal of Animal Science 62:958-967. https://doi.org/10.2527/jas1986.624958x

Brimlow, J. N. and Doyle, S. P. 2014. What do buyers value when making herd sire purchases? An analysis of the premiums paid for genetic and phenotypic differences at a bull consignment auction. Western Economics Forum 13:1-10. https://doi.org/10.22004/ag.econ.252868

Cardoso, F. F. and Lopa, T. M. B. P. (org.). 2010. Pampa Plus: avaliação genética Hereford e Braford. Embrapa Pecuária Sul, Bagé.

Christofari, L. F.; Barcellos, J. O. J.; Costa, E. C.; Oaigen, R. P.; Braccini Neto, J. and Grecellé, R. A. 2008. Tendências na comercialização de bezerros relacionadas às características genéticas no Rio Grande do Sul. Revista Brasileira de Zootecnia 37:171-176. https://doi.org/10.1590/S1516-35982008000100025

Chvosta, J. 1997. The information content of seller-provided presale data in cattle auctions. Thesis (M.Sc.). Montana State University, Bozeman, Montana.

Chvosta, J.; Rucker, R. R. and Watts, M. J. 2001. Transaction costs and cattle marketing: The information content of seller-provided presale data at bull auctions. American Journal of Agricultural Economics 83:286-301. https://doi.org/10.1111/0002-9092.00156

Commer Jr., M.; Couvilllon, W. C.; Herndon Jr., C. W.; Brown, C. J. and Getz, W. R. 1990. The effects of promotion in price determination of beef bulls. The Professional Animal Scientist 6:5-10. https://doi.org/10.15232/S1080- 7446(15)32237-3

Cyrillo, J. N. S. G.; Razook, A. G.; Figueiredo, L. A.; Bonilha Neto, L. M.; Mercadante, M. E. Z. and Tonhati, H. 2001. Estimativas de tendências e parâmetros genéticos do peso padronizado aos 378 dias de idade, medidas corporais e perímetro escrotal de machos Nelore de Sertãozinho, SP. Revista Brasileira de Zootecnia 30:56-65. https://doi.org/10.1590/S1516-35982001000100010

Dhuyvetter, K. C.; Schroeder, T. C.; Simms, D. D.; Bolze Jr., R. P. and Geske, J. 1996. Determinants of purebred beef bull price differentials. Journal of Agricultural and Resource Economics 21:396-410. https://doi.org/10.22004/ag.econ.31030

Eler, J. P.; Ferraz, J. B. S. and Silva, P. R. 1996. Parâmetros genéticos para peso, avaliação visual e circunferência escrotal na raça Nelore, estimados por modelo animal. Arquivo Brasileiro de Medicina Veterinária e Zootecnia 48:203:213.

Evangelista, G. T.; Lopes, J. F.; Fornari, G. B.; Oaigen, R. P.; Goncalves, T. L.; Oliveira, T. E.; Aguiar, L. K. and Barcellos, J. O. J. 2019. Key factors influencing the sale of bulls in livestock auctions. Revista Mexicana de Ciencias Pecuarias 10:610-622. https://doi.org/10.22319/rmcp.v10i3.4609

Frizzas, O. G.; Grossi, D. A.; Buzanskas, M. E.; Paz, C. C. P.; Bezerra, L. A. F.; Lôbo, R. B.; Oliveira, J. A. and Munari, D. P. 2009. Heritability estimates and genetic correlations for body weight and scrotal circumference adjusted to 12 and 18 months of age for male Nellore cattle. Animal 3:347-351. https://doi.org/10.1017/S175173110800373X

=== pág. PDF 20 | rótulo - ===

Holt, J. D.; Fields, D.; Prevatt, J. W. and Kriese-Anderson, L. 2004. Producer valuation of herd bull characteristics. In: 2004 Annual Meeting, August, 1-4, Denver. American Agricultural Economics Association.

Irsik, M.; House, A.; Shuffitt, M. and Shearer, J. 2008. Factors affecting the sale price of bulls consigned to a graded sale. The Bovine Practitioner 42:10-17. https://doi.org/10.21423/bovine-vol42no1p10-17

Jones, R.; Turner, T.; Dhuyvetter, K. C. and Marsh, T. L. 2008. Estimating the economic value of specific characteristics associated with Angus bulls sold at auction. Journal of Agricultural and Applied Economics 40:315-333. https://doi.org/10.1017/S1074070800028133

Koenker, R. and Bassett, G. 1978. Regression quantiles. Econometrica 46:33-50. https://doi.org/10.2307/1913643

Kriese, L. A.; Bertrand, J. K. and Benyshek, L. L. 1991. Genetic and environmental growth trait parameter estimates for Brahman and Brahman-derivative cattle. Journal of Animal Science 69:2362-2370. https://doi. org/10.2527/1991.6962362x

Lowman, B. G.; Scott, N. and Somerville, S. 1976. Condition scoring beef cattle. Technical Bulletin No 6. East of Scotland College of Agriculture, Edinburgh, Scotland.

Magnabosco, C. U.; Lopes, F. B.; Mamede, M. and Sainz, R. D. 2013. Utilização de touros geneticamente avaliados como ferramenta para melhorar a produtividade de sistemas de bovinos de corte. Revista Colombiana de Ciencias Pecuarias 26:284-291.

Maxa, J.; Borchers, N.; Thomsen, H.; Simianer, H.; Gauly, M. and Sharifi, A. R. 2009. Auction price of Texel, Suffolk and German white-headed mutton rams: A genetic-statistical study. Small Ruminant Research 85:105-110. https://doi.org/10.1016/j.smallrumres.2009.07.011

McKiernan, W. 2007. Muscle scoring beef cattle. Primefacts 328:1-5.

Menegassi, S. R. O. and Barcellos, J. O. J. 2015. Aspectos reprodutivos do touro: teoria e prática. Editora Agrolivros, Guaíba.

Menegassi, S. R. O.; Pereira, G. R.; Bremm, C.; Koetz Jr, C.; Lopes, F. G.; Fiorentini, E. C.; McManus, C.; Dias, E. A.; Rocha, M. K.; Lopes, R. B. and Barcellos, J. O. J. 2016. Effects of ambient air temperature, humidity, and wind speed on seminal traits in Braford and Nellore bulls at the Brazilian Pantanal. International Journal of Biometeorology 60:1787-1794. https://doi.org/10.1007/s00484-016-1167-2

NASS/USDA. 2018. National Agricultural Statistics Service Information/United States Department of Agriculture. Available at: <https://www.nass.usda.gov/Charts_and_Maps/Agricultural_Prices/priceca.php>. Accessed on: Feb. 15, 2019.

NESPro. 2015. Informativo NESPro & Embrapa Pecuária Sul: Bovinocultura de corte no Rio Grande do Sul 2(1). UFRGS, Porto Alegre. Available at: <http://www.ufrgs.br/nespro/informativos/2/mobile/index.html>. Accessed on: Dec. 20, 2020.

NESPro. 2018. Informativo NESPro & Embrapa Pecuária Sul: Bovinocultura de corte no Rio Grande do Sul 4(1). UFRGS, Porto Alegre.

NRC - National Research Council. 1996. Nutrient requirements of beef cattle. The National Academies Press, Washington, D.C.

Parkinson, T. J. 2004. Evaluation of fertility and infertility in natural service bulls. The Veterinary Journal 168:215-229. https://doi.org/10.1016/j.tvjl.2003.10.017

Parish, J. A. and Rhinehart, J. D. 2008. Body condition scoring beef cattle. Publication 2508. Mississippi State University. Available at: <https://extension.msstate.edu/sites/default/files/publications/publications/p2508_0.pdf>. Accessed on: Jan. 22, 2019.

Prevatt, C. 2017. Beef cattle market outlook. Available at: <http://animal.ifas.ufl.edu/beef_extension/bcsc/2017/ proceedings/j_prevatt.pdf>. Accessed on: Feb. 16, 2019.

Ríos-Utrera, Á.; Montaño-Bermúdez, M.; Vega-Murillo, V. E.; Martínez-Velázquez, G. and Baeza-Rodríguez, J. J. 2018. Genetic parameters for scrotal circumference, frame score and yearling weight of Mexican Charolais and Charbray young bulls. Revista Colombiana de Ciencias Pecuarias 31:204-212. https://doi.org/10.17533/udea.rccp.v31n3a05

Şentürklü, S.; Landblom, D.; Paisley, S.; Wachenheim, C. and Maddock, R.  2021. Frame score, grazing and delayed feedlot entry effect on performance and economics of beef steers from small-and large-framed cows in an integrated crop-livestock system. Animals 11:3270. https://doi.org/10.3390/ani11113270

Smith, T. 2014. Matching cows and production to the environment. Hereford World, p.32-33. Available at: <https://hereford.org/static/files/0114_CowEfficiency.pdf>. Accessed on: Jan. 16, 2019.

Stock, M. L.; Baldridge, S. L.; Griffin, D. and Coetzee, J. F. 2013. Bovine dehorning – assessing pain and providing analgesic management. Veterinary Clinics of North America: Food Animal Practice 29:103-133. https://doi.org/10.1016/j.cvfa.2012.11.001

Thibier, M. and Wagner, H. G. 2002. World statistics for artificial insemination in cattle. Livestock Production Science 74:203-212. https://doi.org/10.1016/S0301-6226(01)00291-3

=== pág. PDF 21 | rótulo - ===

Torres Júnior, R. A. A.; Bignardi, A. B. and Silva, L. O. C. 2003. Seleção para correção de prepúcio e ausência de prolapso em touros de corte. Documentos, 137. Embrapa Gado de Corte, Campo Grande.

Vestal, M. K.; Lusk, J. L.; DeVuyst, E. A. and Kropp, J. R. 2013. The value of genetic information to livestock buyers: a combined revealed, stated preference approach. Agricultural Economics 44:337-347. https://doi.org/10.1111/agec.12016

Walburger, A. M. 2002. Estimating the implicit prices of beef cattle attributes: a case from Alberta. Canadian Journal of Agricultural Economics 50:135-149. https://doi.org/10.1111/j.1744-7976.2002.tb00424.x
