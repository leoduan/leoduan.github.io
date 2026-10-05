---
layout: default
title: Research
permalink: /research/
---

# Research

My research focuses on the interface between optimization and Bayes: optimization-based priors, optimization-based likelihoods, and optimization-based generative models. Applications are motivated by collaborative work in neuroscience, engineering, forensics, and data privacy.

<p class="legend"><sup>†</sup> Student or trainee I advised</p>

## Preprints

<ul class="pubs">
{% assign preprints = site.data.publications | where: "type", "preprint" %}
{% for pub in preprints %}{% include pub.html pub=pub %}{% endfor %}
</ul>

## Publications

<ul class="pubs">
{% assign journal = site.data.publications | where: "type", "journal" %}
{% for pub in journal %}{% include pub.html pub=pub %}{% endfor %}
</ul>

## Funding & Awards

<ul class="dated">
  <li><span class="when">2023–2027</span><span>NSF-ATD: Geospatial Modeling and Risk Mitigation for Human Movement Dynamics under Hurricane Threats (PI)</span></li>
  <li><span class="when">2024</span><span>UF CLAS Fellowship for Doctoral Student Supervised</span></li>
  <li><span class="when">2022</span><span>UF CLAS Faculty Travel Award</span></li>
  <li><span class="when">2022–2023</span><span>UFII SEED Funding Award</span></li>
  <li><span class="when">2021</span><span>UF Statistics Faculty Award for Doctoral Student Supervised</span></li>
  <li><span class="when">2018</span><span>NeurIPS Bayesian Non-parametrics Award</span></li>
  <li><span class="when">2015</span><span>ASA Paper Competition Award, Section on Bayesian Statistical Science</span></li>
  <li><span class="when">2014</span><span>Woodside Foundation Award for Contribution in Biostatistics and Epidemiology Research</span></li>
</ul>
