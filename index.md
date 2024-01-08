---
layout: default
---



<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.min.css" />
<script src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js"></script>  


# SPRING 2024

## Class Information

Item                     |               
------------------------ | -----------                  
Schedule                 | Tuesdays 6:00 - 7:00 PM Eastern
Location                 | Zoom. Details on Carmen
Professor                | Greg Ryslik / ryslik DOT 1 AT osu DOT edu
Professor Office Hours   | Likely Friday - via zoom. Details on Carmen. Contact me ahead of time if you plan to attend.
TA                       | To be confirmed
TA Office Hours          | To be confirmed
Slack Link				 | See email invite.



## Description: 
This class aims to introduce ways to mine and analyze data for people that are data related fields but are not necessarily computer scientists or data scientists. This webpage will serve as a source of content for the course and will eventually house the homeworks and project code files.
	
It is highly encouraged that you simply fork this entire repo and then just sync updates periodically. This will provide you the easiest access to all the updated code at once. For more information on this process, you can see the documentation [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo). 

## Grading Plan: 
1. Homework x5: 30%
2. Case Studies x4: 40%
3. Final Project: 20%
4. Participation: 10%

There might be tentative bonus points assigned for harder math or cs problems. Max would be at most 2-3% per problem.

## Homeworks
<table class="display" border=1 frame=sides rules=all>
  {% for row in site.data.Homeworks %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ 	pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>

## Case Studies
<table class="display" border=1 frame=sides rules=all>
  {% for row in site.data.Casestudies %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ 	pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>

## Final
<table class="display" border=1 frame=sides rules=all>
  {% for row in site.data.Final %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ 	pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>