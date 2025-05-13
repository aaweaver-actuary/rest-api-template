
## Idea


## Add'l Variables
- unit
- program

## Next steps
- [ ] email Darryl to figure out how he built the data


## Emails
#### 1 - Attributes by NAICS

```
In asking Darryl about the source of those columns, I had hoped that there were just 1-2 steps to produce them, but that’s not the case. In the attached email he describes a daily-run process and then a query that can be run against that, then the actual metrics are finally compiled in a pivot table. It doesn’t filter anything but simply calculates the following:
Hit_Ratio = Hit_Ratio_Numerator/Hit_Ratio_Denominator
Declined_Ratio = Declined_Count/Submission_Count

Clearly at least part of this should be simplified. But I’m inclined just to have Darryl refresh this from time to time, with those final calculated fields happening within his code, rather than having analytics ops rerun some version of this with every call.

-Dan
```

#### 2 - Agency Dashboard Data

- in the following email chain, discussions are laid out about where my source data should come from

```plaintext
The code is part of a process flow but the final (and maybe more relevant to your question) is here:
```

```sas
PROC SQL;
   CREATE TABLE DATA.Submission_NAICS AS 
   SELECT t1.Bound_Status LABEL='' AS Bound_Status, 
          t1.FIRST_INSURED_NAICS_CODE LABEL='' AS NAICS, 
            (substr(t1.FIRST_INSURED_NAICS_CODE,1,3)) AS NAICS_3, 
            (case when Bound_Status='Issued' then 1 else 0 end) AS Hit_Ratio_Numerator, 
            (case when t1.Bound_Status not  in ('Declined', 'Submitted but not quoted') then 1 else 0 end) AS 
            Hit_Ratio_Denominator, 
            (case when t1.Bound_Status='Declined' then 1 else 0 end) AS Declined_Count, 
            (year(t1.SUBMISSION_POLICY_EFFECTIVE_DATE)) AS Effective_Year, 
            (1) AS Submission_Count
      FROM DATA.SUBMISSIONS_2018 t1
      WHERE (CALCULATED Effective_Year) >= 2021;
QUIT;
```
```
The data is here:
/sas/data/project/EG/ActShared/SmallBusiness/RecurringProcess/Small_Business_Hit_Ratio/Data/Submission_NAICS.sas7bdat

This will refresh every day with the Hit Ratio report. Let me know if you need anything else.
```
```
From: Price, Daniel <Daniel_Price@CINFIN.com> 
Sent: Friday, April 25, 2025 9:53 AM
To: Hogue, Darryl <Darryl_Hogue@CINFIN.com>
Subject: RE: Agency Dashboard Data

Since we want to implement something in Analytics Ops, Andy was wondering if that environment could run the query each time. So if we try to go that route, I think it would first be a matter of Andy being able to run it via Python code (if that’s possible), before we try to productionalize it.

For now, could you try to reproduce what you created before? We will certainly want this to be nailed down, even if we arrive at a minimalistic approach to refreshes (such as doing it manually once every 6 months). Then if it’s straightforward to pass the code off to Andy, please do so and copy me.

-Dan
```

```
From: Hogue, Darryl <Darryl_Hogue@CINFIN.com>
Sent: Friday, April 25, 2025 9:47 AM
To: Price, Daniel <Daniel_Price@CINFIN.com>
Subject: RE: Agency Dashboard Data

I searched and it looks like I didn’t save it. I don’t think you have access to Enterprise Submission in the EDW but you should in Snowflake. It shouldn’t be hard to recreate. Do you want to check your access or just have me handle refreshes?
```

```
From: Price, Daniel <Daniel_Price@CINFIN.com> 
Sent: Friday, April 25, 2025 9:20 AM
To: Hogue, Darryl <Darryl_Hogue@CINFIN.com>
Subject: RE: Agency Dashboard Data

Darryl,

Could I get the code used for this data pull? As we try to take these kinds of metrics by NAICS and productionalize them, we might want to rerun such a query regularly. But regardless we will want to rerun from time to time, even if that’s more ad hoc.

-Dan
```

```
From: Hogue, Darryl <Darryl_Hogue@CINFIN.com> 
Sent: Monday, May 13, 2024 2:20 PM
To: Price, Daniel <Daniel_Price@CINFIN.com>; Weishaar, Robert <Robert_Weishaar@cinfin.com>; Kravitz, Max <Max_Kravitz@cinfin.com>; Cable, Laura <Laura_Cable@cinfin.com>
Subject: RE: Agency Dashboard Data

Is this better?
```


```
From: Price, Daniel <Daniel_Price@CINFIN.com> 
Sent: Monday, May 13, 2024 12:59 PM
To: Hogue, Darryl <Darryl_Hogue@CINFIN.com>; Weishaar, Robert <Robert_Weishaar@cinfin.com>; Kravitz, Max <Max_Kravitz@cinfin.com>; Streffon, Laura <Laura_Streffon@cinfin.com>
Subject: RE: Agency Dashboard Data

Two things on this:

•	When we talked about the time to include here the other day, I thought we arrived at something like submissions received in the last 2 years other than the most recent month (since they would be less mature). But what I’m seeing here is policy effective dates within 2024, which is less data and would certainly have some immature submissions.
•	We don’t really need this listed by Submission Identifier, Agency Number, or Insured Name, right? If this is restated, I would recommend it being summarized without granular fields like this.

-Dan
```
```
From: Weishaar, Robert <Robert_Weishaar@cinfin.com> 
Sent: Friday, May 10, 2024 3:54 PM
To: Hogue, Darryl <Darryl_Hogue@CINFIN.com>; Price, Daniel <Daniel_Price@CINFIN.com>; Kravitz, Max <Max_Kravitz@cinfin.com>; Streffon, Laura <Laura_Streffon@cinfin.com>
Subject: RE: Agency Dashboard Data

Nope, early next week is totally fine.  Thank you!
```
```
From: Hogue, Darryl <Darryl_Hogue@CINFIN.com> 
Sent: Friday, May 10, 2024 3:53 PM
To: Weishaar, Robert <Robert_Weishaar@cinfin.com>; Price, Daniel <Daniel_Price@CINFIN.com>; Kravitz, Max <Max_Kravitz@cinfin.com>; Streffon, Laura <Laura_Streffon@cinfin.com>
Subject: RE: Agency Dashboard Data

I see that now… I can add it from the source data. Do you need it today?
```
```
From: Weishaar, Robert <Robert_Weishaar@cinfin.com> 
Sent: Friday, May 10, 2024 3:48 PM
To: Hogue, Darryl <Darryl_Hogue@CINFIN.com>; Price, Daniel <Daniel_Price@CINFIN.com>; Kravitz, Max <Max_Kravitz@cinfin.com>; Streffon, Laura <Laura_Streffon@cinfin.com>
Subject: RE: Agency Dashboard Data

I don’t see NAICS code?
```