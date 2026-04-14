[2202.10739] JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning

# JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning

Michiharu Yamashita1,
Jia Tracy Shen1,
Thanh Tran2,
Hamoon Ekhtiari3,
and Dongwon Lee1

1The Pennsylvania State University, University Park, PA, USA

2Amazon, Cambridge, MA, USA
3FutureFit AI, Toronto, Canada

{michiharu, jqs5443}@psu.edu, tdt@amazon.com, hamoon@futurefit.ai, dongwon@psu.edu

###### Abstract

In online job marketplaces, it is important to establish a well-defined job title taxonomy for various downstream tasks (e.g., job recommendation, users’ career analysis, and turnover prediction). *Job Title Normalization* (*JTN*) is such a cleaning step to classify user-created non-standard job titles into normalized ones.
However, solving the *JTN* problem is non-trivial with challenges:
(1) semantic similarity of different job titles,
(2) non-normalized user-created job titles,
and (3) large-scale and long-tailed job titles in real-world applications.
To this end, we propose a novel solution, named JAMES, that constructs three unique embeddings (i.e., *graph*, *contextual*, and *syntactic*) of a target job title to effectively capture its various traits. We further propose a multi-aspect co-attention mechanism to attentively combine these embeddings, and employ neural logical reasoning representations to collaboratively estimate similarities between messy job titles and normalized job titles in a reasoning space.
To evaluate JAMES, we conduct comprehensive experiments against ten competing models on a large-scale real-world dataset with over 350,000 job titles. Our experimental results show that JAMES significantly outperforms the best baseline by 10.06% in Precision@10 and by 17.52% in NDCG@10, respectively.
To further facilitate the acquisition of normalized job titles for job-domain applications, our JAMES API is available at: https://tinyurl.com/james-job-title-mapping.

###### Index Terms:

multi-aspect embeddings, entity mapping, representation learning, job title normalization

## I Introduction

Background.
The recent proliferation of technology has witnessed an increasing popularity of online professional platforms. These online job marketplaces connect job seekers and companies to find the best match for each other. For example, LinkedIn and Indeed, two of the largest jobs marketplace platforms, have more than 930 million users111https://about.linkedin.com/ and 245 million resumes222https://www.indeed.com/about, respectively.
The vast amount of data available on job marketplaces, including resumes from job seekers and job postings from companies, has spurred companies involved in workforce development, talent intelligence, recruitment, and job search engines to utilize AI techniques to enhance their applications (e.g., job recommendation [[1](#bib.bib1), [2](#bib.bib2)], next career prediction [[3](#bib.bib3), [4](#bib.bib4)], and career analysis [[5](#bib.bib5)]). These AI-powered tools enable job seekers in finding their ideal jobs and companies in recruiting talents that match their roles.
However, the workflow of such job-domain applications involves a critical step, as illustrated in Figure [1](#S1.F1 "Figure 1 ‣ I Introduction ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning"). Before building models for downstream tasks, the various entities found in raw data, especially job titles, must be sorted, consolidated, and normalized. For instance, a position called “systems engineer” in a company A𝐴A and another position called “application programmer” in a company B𝐵B may refer to the same job. Normalizing these two job titles into “software developer” (or noting their compatibility in context) is crucial for job recommendations, career trajectory analysis, and search result expansion. Therefore, the research question (RQ) we investigate is: *How can job titles be automatically normalized*? In particular, we aim to answer this RQ via the framing of the Job Title Normalization (*JTN*) (to be defined in Section 3.1).

![Refer to caption](/html/2202.10739/assets/Figs/downstream_tasks4.png)

Figure 1: Workflow of job-domain applications

Challenges.
Although the *JTN* problem appears simple in nature, addressing it in practice poses several challenges.
First, job titles often bear a semantic closeness to one another that is contingent upon the required skill sets and companies’ own definitions. For example, the job title “data scientist” is prevalent today, and comprises skill sets such as mathematical modeling, statistics, and coding. However, this role can be related to “business analyst” or “data analyst” in some companies, and to “product scientist” in others. Thus, comparing job titles alone is inadequate for solving *JTN*, and it is necessary to represent them in a semantic space to ensure accurate calibration.
Second, job titles collected from users’ resumes are often untidy due to non-standard naming conventions and auxiliaries. The job title “software developer” in one resume can be written as “SDE” in another. Moreover, creative job titles such as “data geek” or “strategic futurist” that individuals may list on their resumes do not necessarily appear in an industry-wide job title taxonomy.
Third, while an industry job taxonomy contains only a few hundred to a few thousand job titles, the number of job titles encountered on job marketplace platforms is orders of magnitude larger. Nevertheless, existing solutions have only employed either small-scale datasets or company-created datasets (as opposed to user-written), in which *JTN* was addressed through manual labeling/cleaning or text normalization procedures. For instance, Zhang et al. [[6](#bib.bib6)] employed a dataset with only 26 unique job titles for similar expertise job matching, while Dave et al. [[7](#bib.bib7)] used a dataset of 4,325 unique job titles for job and skill recommendation tasks. More recently Li et al. [[8](#bib.bib8)] developed a job title taxonomy containing 30,000 entries on LinkedIn for a job understanding task. However, the challenges inherent in *JTN* for the vast number of job titles still remain inadequately addressed.

Ideas.
To address the aforementioned challenges in *JTN*, we propose JAMES (Job title mApping with Multi-aspect Embeddings and reaSoning), and demonstrates its effectiveness using a real-world career dataset containing more than 350,000 job titles. Specifically, JAMES considers three unique multi-aspect (i.e., graph, contextual, and syntactic) embeddings for candidate job titles.
First, we establish a graph embedding to represent the latent topological job title similarity based on users’ job transitions, exploiting the fact that users typically switch to similar positions or titles (i.e., changing from “data scientist” to “chef” is highly unlikely although possible). We use a hyperbolic graph embedding for the latent knowledge dependencies in a job title hierarchy, as it outperforms Euclidean graph embeddings on hierarchical structure datasets [[9](#bib.bib9), [10](#bib.bib10)]. In addition, hyperbolic graph embeddings help mitigate the problem of incomplete and inconsistent job transition patterns by providing a smaller distortion and an exponential expansion of nodes [[11](#bib.bib11), [10](#bib.bib10)].
Second, we leverage a pretrained BERT embedding to account for the contextual similarity between two candidate job titles, which can identify contextually-related job titles, as language models can measure the contextual and semantic distance.
Third, we create a syntactic embedding to capture the string-to-string similarity between two input job titles, allowing for the detection of misspelled (e.g., “electric engieer”) and user-created (e.g., “cool data scientist”) job titles.
Also, we design a neural collaborative reasoning [[12](#bib.bib12)] that takes multi-aspect embeddings as input and produces reasoning-based multi-aspect embeddings to mitigate uncertainty among standard job titles, covering job titles that are not accurately captured by either contextual or syntactic embeddings.
After building multi-aspect embeddings using our large-scale resume dataset, we develop a multi-aspect co-attention mechanism that considers all three multi-aspect embeddings concurrently.

Contributions.
Our contributions are as follows:

* •

  We use a large-scale, real-world, and user-generated dataset from a career platform (FutureFit AI), which comprises over 350,000 unique job titles, for the job-domain specific preprocessing task, *Job Title Normalization* (*JTN*).
* •

  To solve the *JTN* task, we propose a novel model, JAMES, that employs multi-aspect embeddings and reasoning representations accounting for *graph*, *contextual*, and *syntactic* embeddings.
* •

  We conduct extensive experiments and demonstrate the effectiveness of JAMES against ten competing baseline models. JAMES significantly outperforms the best baseline by 10.06% in Precision@10 and by 17.52% in NDCG@10, respectively. We also apply JAMES to other downstream tasks and report the findings and further implications.
* •

  We develop and release JAMES API publicly, allowing for the acquisition of normalized job titles from job title entities.

## II Related Work

### II-A Job Title Classification

Previously, *JTN* was often overlooked and just addressed through manual labeling or simple data preprocessing. However, there have been several prior works that attempt to solve it as a task of job title classification [[13](#bib.bib13), [14](#bib.bib14)]. Wang et al. [[15](#bib.bib15)] proposed a CNN-based approach that developed text vectors using a job description dataset, while Zhu et al. [[16](#bib.bib16)] built a KNN model using Word2Vec. While such methods using job descriptions can be helpful, in the real world, it is often difficult to obtain access to all companies’ job description datasets, and the applicability of such methods to user-generated job titles extracted from resumes is not well understood. Therefore, our work aims to develop a practical solution applicable to a user-generated dataset (i.e., resumes).

As a job entity benchmarking, Luo et al. [[17](#bib.bib17)] created a job transition graph using Random Walk-based vectors, and indicated the potential of job graph embedding. Zhang et al. [[18](#bib.bib18)] proposed Job2Vec as a job title benchmarking tool based on job records. However, both works were only validated in link and/or node prediction and not specifically designed for *JTN*, resulting in uncertainty regarding their applicability to *JTN* and normalization. Moreover, Job2Vec aimed to link job titles of the same expertise level to calibrate salaries for recruiters [[18](#bib.bib18)]. While these benchmarks could be used for job title clustering, they manually filtered out low-frequency words in job titles as a data preprocessing step, and limited their dataset to the IT and finance domains, which restricts the generalizability of their representations to real-world scenarios. Additionally, only 15 well-known companies such as Google and Microsoft were chosen in their IT dataset, which may not reflect a practical scenario where companies or individuals want to map all job titles from users’ resumes into normalized ones.
In contrast, our study focuses on a realistic and large-scale setting for *JTN*, utilizing a dataset from 165,086 unique companies across all sectors. Our approach differs from previous works as we employ contextual embeddings to capture the potential meaning of words, and syntactic embeddings to detect misspelled and user-created words, addressing issues not considered in prior works. Furthermore, we use reasoning to obtain more robust representations.

### II-B Representation Learning in Job Domain

Liu et al. [[19](#bib.bib19)] conducted career path prediction using multiple social media.
For job skill representation, Shi et al. [[20](#bib.bib20)] developed “Job2Skills”, a market-aware skill extraction system, which considers the salient level of a skill and extracts important skill entities from job postings and target members using multi-resolution.
Qin et al. [[21](#bib.bib21)] developed a person-job fit model that applied a word-level semantic representation for both job requirements and job seekers’ experiences based on RNN.
Yamashita et al. [[22](#bib.bib22)] proposed a long-term career path prediction from large-scale resumes with multiple embeddings.
While these studies relied on job-domain entities, our JAMES can be applied to such job-domain applications to normalize job titles.

### II-C Hyperbolic Machine Learning

Hyperbolic geometry is a non-Euclidean geometry that focuses on spaces of constant negative Gaussian curvature. Hyperbolic space has been used to develop embedding and machine learning models for hierarchical and graph structures, due to its benefits such as embedding on smaller dimensions [[10](#bib.bib10)]. Poincare embedding, proposed by Nickel et al. [[9](#bib.bib9)], enables hierarchical data to be represented better than Euclidean embeddings. Chami et al. [[11](#bib.bib11)] developed a hyperbolic technique for graph convolutional networks. In the case of career trajectory datasets, they can be represented as graphs, as done by Zhang et al. [[6](#bib.bib6)]. However, to the best of our knowledge, our work is the first to apply hyperbolic geometry to career transition data. Since hyperbolic embeddings work well on tree-structured datasets, we consider hyperbolic embeddings to be effective for representing latent knowledge dependencies in job titles, which are often hierarchical (e.g., junior, senior, VP). Hence, we incorporate hyperbolic embeddings into our model and compare the baselines.

## III Preliminary

TABLE I: Definition of our notations in this paper

|  |  |
| --- | --- |
| Notation | Definition |
| j𝑗j | job title from resume |
| 𝒳𝒳\mathcal{X} | a set of job titles from all resumes |
| v𝑣v | normalized job title from the ground truth |
| 𝒴𝒴\mathcal{Y} | a set of normalized job titles from the ground truth |
| 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\; | hyperbolic graph embeddings |
| 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\; | BERT embeddings |
| 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\; | syntactic (string similarity) embeddings |
| A(h​b)superscript𝐴ℎ𝑏A^{(hb)}\; | affinity matrices between 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\; |
| A(h​s)superscript𝐴ℎ𝑠A^{(hs)}\; | affinity matrices between 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\; |
| A(b​s)superscript𝐴𝑏𝑠A^{(bs)}\; | affinity matrices between 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\; |
| W(h​b)superscript𝑊ℎ𝑏W^{(hb)}\; | learnable weights between 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\; |
| W(h​s)superscript𝑊ℎ𝑠W^{(hs)}\; | learnable weights between 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\; |
| W(b​s)superscript𝑊𝑏𝑠W^{(bs)}\; | learnable weights between 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\; |
| Khsubscript𝐾ℎK\_{h}\; | attention graph for 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;, acknowledging supports from the other embedding views 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;through A(h​b)superscript𝐴ℎ𝑏A^{(hb)}\;and A(h​s)superscript𝐴ℎ𝑠A^{(hs)}\; |
| Kbsubscript𝐾𝑏K\_{b}\; | attention graph for 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;, acknowledging supports from the other embedding views 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;through 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and A(h​s)superscript𝐴ℎ𝑠A^{(hs)}\; |
| Kssubscript𝐾𝑠K\_{s}\; | attention graph for 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;, acknowledging supports from the other embedding views 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;and 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;through A(h​b)superscript𝐴ℎ𝑏A^{(hb)}\;and 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\; |
| 𝑿^𝒉subscriptbold-^𝑿𝒉\boldsymbol{\hat{X}\_{h}}\; | co-attentive multi-view embeddings from 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\; |
| 𝑿^𝒃subscriptbold-^𝑿𝒃\boldsymbol{\hat{X}\_{b}}\; | co-attentive multi-view embeddings from 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\; |
| 𝑿^𝒔subscriptbold-^𝑿𝒔\boldsymbol{\hat{X}\_{s}}\; | co-attentive multi-view embeddings from 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\; |
| 𝑿𝒃′subscriptsuperscript𝑿bold-′𝒃\boldsymbol{{X}^{\prime}\_{b}}\; | reasoning-based representation from 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\; |
| 𝑿𝒔′subscriptsuperscript𝑿bold-′𝒔\boldsymbol{{X}^{\prime}\_{s}}\; | reasoning-based representation from 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\; |

Major notations used throughout the paper are summarized in Table [I](#S3.T1 "TABLE I ‣ III Preliminary ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning").
In this section, we describe a definition of the problem, Job Title Normalization (*JTN*), and our dataset.

### III-A Problem Definition

We formally define the *JTN* task as follows:

Note that during the training of the mapping function f​(⋅)𝑓⋅f(\cdot), we consider the *JTN* task as a multi-class classification task. During the inference, with each ji∈𝒳subscript𝑗𝑖𝒳j\_{i}\in\mathcal{X}, we take the output probability distribution over all normalized job titles vk∈𝒴subscript𝑣𝑘𝒴v\_{k}\in\mathcal{Y} as the ranking scores to output *top-k* most similar job titles vk∈𝒴subscript𝑣𝑘𝒴v\_{k}\in\mathcal{Y}.

### III-B Dataset

We obtained the dataset from a popular career platform
FutureFit AI333https://www.futurefit.ai/,
which partners globally with other companies and governments to assist employees in navigating career transitions. We randomly selected over 400,000 resumes from the platform, which had at least five valid working experiences in the United States (i.e., a path with five nodes in a job transition graph). This was done to ensure that the job transition graph was meaningful, while also being reasonably large. Table [II](#S3.T2 "TABLE II ‣ III-B Dataset ‣ III Preliminary ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") presents a summary of our dataset information, including the average length of words and characters in job titles.

Our dataset contains 354,168 unique job titles from 165,086 unique companies, and more than 2.7 million job transition trajectories. To solve the *JTN* task, we only extract the job seeker’s basic information from their resume, such as company ID, job title, start and end dates of working, while ensuring that all private employee information is anonymized. On average, job titles have 4.15 words and 28.9 characters. The top five most frequent job titles are sales associate (0.33%), research assistant (0.23%), administrative assistant (0.23%), project manager (0.19%), and CEO (0.18%).
Our dataset will be available upon request.

In comparison to previous works [[6](#bib.bib6), [7](#bib.bib7), [23](#bib.bib23), [18](#bib.bib18)], our dataset has a significantly larger number of job titles. Specifically, our dataset contains over 11,500 times more job titles than [[6](#bib.bib6)], over 69 times more job titles than [[7](#bib.bib7)], over 30 times more job titles than [[23](#bib.bib23)], and four times more job titles than the Job2Vec (Finance) dataset [[18](#bib.bib18)].
To create our ground truth dataset, we perform an exact search to match job titles in our dataset with the European Skills/Competences, qualifications, and Occupations (ESCO) taxonomy444https://ec.europa.eu/esco/portal/escopedia/ESCO, which provides a hierarchical structure of job titles and normalized job titles as job groups. For example, “software developers” consists of “application developer”, “software engineer”, “software architect”, etc. We remove proper nouns from the job titles, and use the matched job titles as the ground truth labels for our experiments.

TABLE II: Our large-scale resume dataset

|  |  |
| --- | --- |
| # of Resumes | 401,253 |
| # of Job Titles | 354,168 |
| # of Companies | 165,086 |
| # of Transitions | 2,738,403 |
| Average length of words | 4.15 |
| Average length of characters | 28.9 |

## IV Our Proposed Model: JAMES

![Refer to caption](/html/2202.10739/assets/Figs/toy.png)

Figure 2: Toy example of JAMES in *Job Title Normalization*.

![Refer to caption](/html/2202.10739/assets/Figs/model_overview.png)

Figure 3: Model overview of JAMES.

In this section, we describe our job title normalization model, JAMES. The main idea of JAMES is to learn multi-aspect representations of an input job title and produce its corresponding *top-n* normalized standard job title mappings that are predefined in a standard job title taxonomy. Figure [2](#S4.F2 "Figure 2 ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") shows a toy example of how JAMES works. First, the job titles of a resume are extracted. Next, JAMES learns the multi-aspect embeddings, including graph, semantic, and syntactic embeddings, for each job title. In this example, the input job title is “mobile app speciallist”, and JAMES utilizes the multi-aspect embeddings to predict the matching standard job title, resulting in “applications programmer”.

Figure [3](#S4.F3 "Figure 3 ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") provides a more detailed overview of JAMES. To learn the graph embeddings of the input job title, JAMES employ the state-of-the-art hyperbolic graph representation learning. To learn the semantic embeddings of the input job title, JAMES use the well-known pretrained BERT. To obtain the syntactic embeddings of the input job title, JAMES encodes a dense embedding vector with a size equal to the number of standard job titles. Each element in the vector represents the string-based similarity score between the input job title and the corresponding standard job title. Next, we propose a multi-aspect co-attention mechanism that assigns attention scores to the three multi-aspect embeddings. We also introduce a reasoning-based module in JAMES that collaboratively reasons the multi-aspect embeddings in a reasoning space. Finally, JAMES fuses all the output embeddings to produce the *top-n* mapping normalized job titles for the input job title as outputs. We provide a detailed description of JAMES in the following subsections.

### IV-A Multi-Aspect Embeddings

#### IV-A1 Hyperbolic Graph Embedding

![Refer to caption](/html/2202.10739/assets/Figs/hge.png)

Figure 4: Architecture for hyperbolic graph embedding.

![Refer to caption](/html/2202.10739/assets/Figs/gcn_viz.png)

(a) Euclidean embedding

![Refer to caption](/html/2202.10739/assets/Figs/hgcn_viz.png)

(b) Hyperbolic embedding

Figure 5: Example visualizations for the Euclidean and Hyperbolic embeddings from job transition graph.

To construct a hyperbolic graph embedding that captures the topological features of our career trajectory dataset, we first create a job transition graph, as illustrated in Figure [4](#S4.F4 "Figure 4 ‣ IV-A1 Hyperbolic Graph Embedding ‣ IV-A Multi-Aspect Embeddings ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning"). We define nodes as job titles and links as the transitions between the job titles, where each link is directed and asymmetric. For instance, if a person changes their job title from “Software Engineer” (SWE) to “Machine Learning Engineer” (MLE), the graph has a directed link from SWE to MLE.

The job transition graph is defined as G=(V,E,W)𝐺𝑉𝐸𝑊G=(V,E,W), where V𝑉V is the set of job titles (i.e., nodes), E𝐸E is the set of job transitions (i.e., links in the graph), and W𝑊W is the set of link weights. The job transition weight Wi,jsubscript𝑊

𝑖𝑗W\_{i,j} is formulated as Wi,j=ei,j/∑i=1n∑j=1nei,jsubscript𝑊

𝑖𝑗subscript𝑒

𝑖𝑗superscriptsubscript𝑖1𝑛superscriptsubscript𝑗1𝑛subscript𝑒

𝑖𝑗W\_{i,j}=e\_{i,j}/\sum\_{i=1}^{n}\sum\_{j=1}^{n}e\_{i,j}, where ei,jsubscript𝑒

𝑖𝑗e\_{i,j} is the number of transitions from node visubscript𝑣𝑖v\_{i} to node vjsubscript𝑣𝑗v\_{j}. Based on all job transitions, we construct a graph and derive graph embeddings. To build the hyperbolic graph, we consider a head node (i.e., more recent user’s career) as the parent and a tail node (i.e., the previous career) as the child, assuming that the most recent job title contains all the requirements and skill sets from the previous job titles. We then embed the nodes in hyperbolic space using Poincare embedding [[9](#bib.bib9)] as a hyperbolic embedding and train a Poincare ball model from the relations of nodes in the graph.

Since the Poincare ball is a Riemannian manifold, the Riemannian metric tensor is represented in the d𝑑d-dimentional ball Bd={x∈ℝd|‖x‖<1}superscript𝐵𝑑conditional-set𝑥superscriptℝ𝑑norm𝑥1B^{d}=\{x\in\mathbb{R}^{d}|||x||<1\}, where ‖x‖norm𝑥||x|| is the
Euclidean norm. Then, the Riemannian metric tensor rxsubscript𝑟𝑥r\_{x} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rx=(21−‖x‖2)2rEr\_{x}=\Bigl{(}\frac{2}{1-||x||^{2}}\Bigl{)}^{2}r^{E} |  | (1) |

where x∈Bd𝑥superscript𝐵𝑑x\in B^{d} and rEsuperscript𝑟𝐸r^{E} is the Euclidean metric tensor. Then, the distance of two points a,b∈Bd

𝑎𝑏
superscript𝐵𝑑a,b\in B^{d} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d(a,b)=arcosh(1+2‖a−b‖2(1−‖a‖2)​(1−‖b‖2))d(a,b)=arcosh\Bigl{(}1+2\frac{||a-b||^{2}}{(1-||a||^{2})(1-||b||^{2})}\Bigl{)} |  | (2) |

Based on these metrics, we construct the Poincare embedding on the Poincare ball [[9](#bib.bib9)] with the input of the parent-child pair dataset and obtain the m𝑚m-dimensional embedding. Figure [5](#S4.F5 "Figure 5 ‣ IV-A1 Hyperbolic Graph Embedding ‣ IV-A Multi-Aspect Embeddings ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") provides a visualization comparison between Euclidean and Poincare embeddings in a 2-dimensional ball, where the hyperbolic embedding exhibits a hierarchy of dots, while each dot in the Euclidean embedding is scattered disorderly. We output 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;as the hyperbolic graph embedding of each input job title.

#### IV-A2 BERT Embedding

![Refer to caption](/html/2202.10739/assets/Figs/bert.png)

Figure 6: Learning semantic embeddings of the input job tile via the pretrained uncased BERT-base.

To address the issue of different job titles referring to the same position (e.g., “Data Analyst” vs “Data Scientist”), we learn the semantic embeddings of the input job titles using the pre-trained BERT [[24](#bib.bib24)]. Specifically, we use the pre-trained DistilRoBERTa on SBERT [[25](#bib.bib25)] due to its efficiency and effectiveness.

The architecture for the BERT embedding is illustrated in Figure [6](#S4.F6 "Figure 6 ‣ IV-A2 BERT Embedding ‣ IV-A Multi-Aspect Embeddings ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning"). For each input job title, we first tokenize it into wordpieces using the BERT-base uncased tokenizer. Then, we use the pretrained BERT-base uncased embeddings to obtain the embeddings 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;of the [CLS] token as the final representations of the input job title.

#### IV-A3 Syntactic Embedding

![Refer to caption](/html/2202.10739/assets/Figs/string.png)

Figure 7: Architecture for syntactic (string similarity) embedding. Given the input job title “*mobile app specialist*”, we represent it by an embedding vector 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;∈ℛ|𝒴|absentsuperscriptℛ𝒴\in\mathcal{R}^{|\mathcal{Y}|}, where 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;[k] = *cosine-sim*(“*mobile app specialist*”, vksubscript𝑣𝑘v\_{k}), with vk∈subscript𝑣𝑘absentv\_{k}\in 𝒴𝒴\mathcal{Y}.

To capture the syntactic representation of job titles, we use cosine similarity to score the string similarity between an input job title and all of the normalized job titles in the job taxonomy (i.e., ESCO). Figure [7](#S4.F7 "Figure 7 ‣ IV-A3 Syntactic Embedding ‣ IV-A Multi-Aspect Embeddings ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") shows the architecture for this embedding. We calculate all pairs between job titles and their parent job titles, and define the similarity matrix as the syntactic representation.

For a given set of
𝒳𝒳\mathcal{X} input job titles and 𝒴𝒴\mathcal{Y} predefined normalized job titles in the job taxonomy, the syntactic embedding of a job title s𝑠s ∈\in 𝒳𝒳\mathcal{X} is a vector 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}} of 𝒴𝒴\mathcal{Y} dimensions, where each dimension indicates the string-string cosine similarity with a character-level comparison between s𝑠s and each corresponding normalized job title in 𝒴𝒴\mathcal{Y}. For example, 𝑿𝒔​[0]=cosine-sim​(s,v0)subscript𝑿𝒔delimited-[]0cosine-sim𝑠subscript𝑣0\boldsymbol{X\_{s}}[0]=\text{cosine-sim}(s,v\_{0}), 𝑿𝒔​[1]=cosine-sim​(s,v1)subscript𝑿𝒔delimited-[]1cosine-sim𝑠subscript𝑣1\boldsymbol{X\_{s}}[1]=\text{cosine-sim}(s,v\_{1}), …, 𝑿𝒔​[|𝒴|−1]=cosine-sim​(s,v|𝒴|−1)subscript𝑿𝒔delimited-[]𝒴1cosine-sim𝑠subscript𝑣𝒴1\boldsymbol{X\_{s}}[|\mathcal{Y}|-1]=\text{cosine-sim}(s,v\_{|\mathcal{Y}|-1}). We define the resulting syntactic embeddings as 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;.

### IV-B Multi-Aspect Co-Attention

In the previous sections, we extract three discrete embeddings for an input job title: (i) hyperbolic graph embeddings 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;, (ii) BERT embeddings 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;, and (iii) syntactic embeddings 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;. However, the embeddings are learned separately and may have redundant features. To address this issue, we aim to learn multi-aspect embeddings that incorporate all three embeddings and are attentive to each other. For this purpose, a traditional method is to weigh each embedding view by hierarchical attention [[26](#bib.bib26)], where the 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;can be used as query, 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;can be used as key/value. Then the 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and the attentive 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;can be combined as a query, and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;can be used as key/value. As the hierarchical attention is performed sequentially and is not practical for large-scale datasets with millions of job titles. Therefore, we extend the traditional co-attention mechanism [[27](#bib.bib27)] which takes only two input sources, and propose a multi-aspect co-attention mechanism that can work for p𝑝p inputs (i.e., p≥2𝑝2p\geq 2). In this sense, our multi-aspect co-attention mechanism uses k−1𝑘1k-1 views to guide the attention weights for the left-over view in parallel.

![Refer to caption](/html/2202.10739/assets/Figs/coatt.png)

Figure 8: Architecture for Multi-view Co-attention.

Figure [8](#S4.F8 "Figure 8 ‣ IV-B Multi-Aspect Co-Attention ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") shows the architecture for our multi-aspect co-attention.
We start by computing three affinity matrices for three pairs of two embedding views: A(h​b)superscript𝐴ℎ𝑏A^{(hb)}\;between 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;, A(h​s)superscript𝐴ℎ𝑠A^{(hs)}\;between 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;, and A(b​s)superscript𝐴𝑏𝑠A^{(bs)}\;between 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;. Specifically, the affinity matrices, A(h​b)superscript𝐴ℎ𝑏A^{(hb)}\;, A(h​s)superscript𝐴ℎ𝑠A^{(hs)}\;, and A(b​s)superscript𝐴𝑏𝑠A^{(bs)}\;are calculated as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A(h​b)superscript𝐴ℎ𝑏\displaystyle A^{(hb)} | =tanh​(𝑿𝒉​W(h​b)​𝑿𝒃T)absenttanhsubscript𝑿𝒉superscript𝑊ℎ𝑏superscriptsubscript𝑿𝒃𝑇\displaystyle=\text{tanh}\big{(}\boldsymbol{X\_{h}}W^{(hb)}\boldsymbol{X\_{b}}^{T}\big{)} |  | (3) |
|  | A(h​s)superscript𝐴ℎ𝑠\displaystyle A^{(hs)} | =tanh​(𝑿𝒉​W(h​s)​𝑿𝒔T)absenttanhsubscript𝑿𝒉superscript𝑊ℎ𝑠superscriptsubscript𝑿𝒔𝑇\displaystyle=\text{tanh}\big{(}\boldsymbol{X\_{h}}W^{(hs)}\boldsymbol{X\_{s}}^{T}\big{)} |  |
|  | A(b​s)superscript𝐴𝑏𝑠\displaystyle A^{(bs)} | =tanh​(𝑿𝒃​W(b​s)​𝑿𝒔T)absenttanhsubscript𝑿𝒃superscript𝑊𝑏𝑠superscriptsubscript𝑿𝒔𝑇\displaystyle=\text{tanh}\big{(}\boldsymbol{X\_{b}}W^{(bs)}\boldsymbol{X\_{s}}^{T}\big{)} |  |

, where W(h​b)superscript𝑊ℎ𝑏W^{(hb)}\;, W(h​s)superscript𝑊ℎ𝑠W^{(hs)}\;, and W(b​s)superscript𝑊𝑏𝑠W^{(bs)}\;are learnable weights. Next, we measure the weight Khsubscript𝐾ℎK\_{h}\;for 𝑿𝒉subscript𝑿𝒉\boldsymbol{X\_{h}}\;, acknowledging supports from the other embedding views 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;and 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;through A(h​b)superscript𝐴ℎ𝑏A^{(hb)}\;and A(h​s)superscript𝐴ℎ𝑠A^{(hs)}\;as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kh=tanh​(Wh​𝑿𝒉+Wb​h​(A(h​b)​𝑿𝒃)+Ws​h​(A(h​s)​𝑿𝒔))subscript𝐾ℎtanhsubscript𝑊ℎsubscript𝑿𝒉subscript𝑊𝑏ℎsuperscript𝐴ℎ𝑏subscript𝑿𝒃subscript𝑊𝑠ℎsuperscript𝐴ℎ𝑠subscript𝑿𝒔K\_{h}=\text{tanh}\big{(}W\_{h}\boldsymbol{X\_{h}}+W\_{bh}(A^{(hb)}\boldsymbol{X\_{b}})+W\_{sh}(A^{(hs)}\boldsymbol{X\_{s}})\big{)} |  | (4) |

In the same manner, we compute the weights Kbsubscript𝐾𝑏K\_{b}\;for 𝑿𝒃subscript𝑿𝒃\boldsymbol{X\_{b}}\;, and Kssubscript𝐾𝑠K\_{s}\;for 𝑿𝒔subscript𝑿𝒔\boldsymbol{X\_{s}}\;as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kb=tanh​(Wb​𝑿𝒃+Wh​b​(A(h​b)​𝑿𝒉)+Ws​b​(A(b​s)​𝑿𝒔))subscript𝐾𝑏tanhsubscript𝑊𝑏subscript𝑿𝒃subscript𝑊ℎ𝑏superscript𝐴ℎ𝑏subscript𝑿𝒉subscript𝑊𝑠𝑏superscript𝐴𝑏𝑠subscript𝑿𝒔\displaystyle K\_{b}=\text{tanh}\big{(}W\_{b}\boldsymbol{X\_{b}}+W\_{hb}(A^{(hb)}\boldsymbol{X\_{h}})+W\_{sb}(A^{(bs)}\boldsymbol{X\_{s}})\big{)} |  | (5) |
|  | Ks=tanh​(Ws​𝑿𝒔+Wh​s​(A(h​s)​𝑿𝒉)+Wb​s​(A(b​s)​𝑿𝒃))subscript𝐾𝑠tanhsubscript𝑊𝑠subscript𝑿𝒔subscript𝑊ℎ𝑠superscript𝐴ℎ𝑠subscript𝑿𝒉subscript𝑊𝑏𝑠superscript𝐴𝑏𝑠subscript𝑿𝒃\displaystyle K\_{s}=\text{tanh}\big{(}W\_{s}\boldsymbol{X\_{s}}+W\_{hs}(A^{(hs)}\boldsymbol{X\_{h}})+W\_{bs}(A^{(bs)}\boldsymbol{X\_{b}})\big{)} |  |

Then, the co-attentive multi-aspect embeddings 𝑿^𝒉subscriptbold-^𝑿𝒉\boldsymbol{\hat{X}\_{h}}\;, 𝑿^𝒃subscriptbold-^𝑿𝒃\boldsymbol{\hat{X}\_{b}}\;and 𝑿^𝒔subscriptbold-^𝑿𝒔\boldsymbol{\hat{X}\_{s}}\;can be computed as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑿^𝒉subscriptbold-^𝑿𝒉\displaystyle\boldsymbol{\hat{X}\_{h}} | =s​o​f​t​m​a​x​(Kh)⊙𝑿𝒉absentdirect-product𝑠𝑜𝑓𝑡𝑚𝑎𝑥subscript𝐾ℎsubscript𝑿𝒉\displaystyle={softmax}(K\_{h})\odot\;\boldsymbol{X\_{h}} |  | (6) |
|  | 𝑿^𝒃subscriptbold-^𝑿𝒃\displaystyle\boldsymbol{\hat{X}\_{b}} | =s​o​f​t​m​a​x​(Kb)⊙𝑿𝒃absentdirect-product𝑠𝑜𝑓𝑡𝑚𝑎𝑥subscript𝐾𝑏subscript𝑿𝒃\displaystyle={softmax}(K\_{b})\odot\boldsymbol{X\_{b}} |  |
|  | 𝑿^𝒔subscriptbold-^𝑿𝒔\displaystyle\boldsymbol{\hat{X}\_{s}} | =s​o​f​t​m​a​x​(Ks)⊙𝑿𝒔absentdirect-product𝑠𝑜𝑓𝑡𝑚𝑎𝑥subscript𝐾𝑠subscript𝑿𝒔\displaystyle={softmax}(K\_{s})\odot\;\boldsymbol{X\_{s}} |  |

where ⊙direct-product\odot is the element-wise product.

### IV-C Reasoning-based Representations

TABLE III:
Neural Logical Regularizations. The NOT module is implemented by an one-layer MLP, and the OR module is implemented by another one-layer MLP. The *True* and *False* are logical constants in the traditional logical equations, but are learnable representations in our neural logical reasoning modules.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Logical Rule | Equation | Neural Logical Regularization. |
| NOT | Negation | ¬T​r​u​e=F​a​l​s​e𝑇𝑟𝑢𝑒𝐹𝑎𝑙𝑠𝑒\neg True=False | r1=∑j∈𝒳s​i​m​(j,N​O​T​(j))+∑v∈𝒴s​i​m​(v,N​O​T​(v))subscript𝑟1subscript𝑗𝒳𝑠𝑖𝑚𝑗𝑁𝑂𝑇𝑗subscript𝑣𝒴𝑠𝑖𝑚𝑣𝑁𝑂𝑇𝑣r\_{1}=\sum\_{j\in\mathcal{X}}sim(j,NOT(j))+\sum\_{v\in\mathcal{Y}}sim(v,NOT(v)) |
| Double Negation | ¬(¬j)=j𝑗𝑗\neg(\neg j)=j | r2=∑j∈𝒳(1−s​i​m​(j,N​O​T​(N​O​T​(j))))+∑v∈𝒴(1−s​i​m​(v,N​O​T​(N​O​T​(v))))subscript𝑟2subscript𝑗𝒳1𝑠𝑖𝑚𝑗𝑁𝑂𝑇𝑁𝑂𝑇𝑗subscript𝑣𝒴1𝑠𝑖𝑚𝑣𝑁𝑂𝑇𝑁𝑂𝑇𝑣r\_{2}=\sum\_{j\in\mathcal{X}}\big{(}1-sim(j,NOT(NOT(j)))\big{)}+\sum\_{v\in\mathcal{Y}}\big{(}1-sim(v,NOT(NOT(v)))\big{)} |
| OR | Identity | j∨F​a​l​s​e=j𝑗𝐹𝑎𝑙𝑠𝑒𝑗j\;\vee\;False=j | r3=∑j∈𝒳(1−s​i​m​(O​R​(j,F​a​l​s​e),j))+∑v∈𝒴(1−s​i​m​(O​R​(v,F​a​l​s​e),v))subscript𝑟3subscript𝑗𝒳1𝑠𝑖𝑚𝑂𝑅𝑗𝐹𝑎𝑙𝑠𝑒𝑗subscript𝑣𝒴1𝑠𝑖𝑚𝑂𝑅𝑣𝐹𝑎𝑙𝑠𝑒𝑣r\_{3}=\sum\_{j\in\mathcal{X}}\big{(}1-sim(OR(j,False),j)\big{)}+\sum\_{v\in\mathcal{Y}}\big{(}1-sim(OR(v,False),v)\big{)} |
| Annihilator | j∨T​r​u​e=T​r​u​e𝑗𝑇𝑟𝑢𝑒𝑇𝑟𝑢𝑒j\;\vee\;True=True | r4=∑j∈𝒳(1−s​i​m​(O​R​(j,T​r​u​e),T​r​u​e))+∑v∈𝒴(1−s​i​m​(O​R​(v,T​r​u​e),T​r​u​e))subscript𝑟4subscript𝑗𝒳1𝑠𝑖𝑚𝑂𝑅𝑗𝑇𝑟𝑢𝑒𝑇𝑟𝑢𝑒subscript𝑣𝒴1𝑠𝑖𝑚𝑂𝑅𝑣𝑇𝑟𝑢𝑒𝑇𝑟𝑢𝑒r\_{4}=\sum\_{j\in\mathcal{X}}\big{(}1-sim(OR(j,True),True)\big{)}+\sum\_{v\in\mathcal{Y}}\big{(}1-sim(OR(v,True),True)\big{)} |
| Idempotence | j∨j=j𝑗𝑗𝑗j\;\vee\;j=j | r5=∑j∈𝒳(1−s​i​m​(O​R​(j,j),j))+∑v∈𝒴(1−s​i​m​(O​R​(v,v),v))subscript𝑟5subscript𝑗𝒳1𝑠𝑖𝑚𝑂𝑅𝑗𝑗𝑗subscript𝑣𝒴1𝑠𝑖𝑚𝑂𝑅𝑣𝑣𝑣r\_{5}=\sum\_{j\in\mathcal{X}}\big{(}1-sim(OR(j,j),j)\big{)}+\sum\_{v\in\mathcal{Y}}\big{(}1-sim(OR(v,v),v)\big{)} |
| Complementation | j∨¬j=T​r​u​e𝑗𝑗𝑇𝑟𝑢𝑒j\;\vee\;\neg j=True | r6=∑j∈𝒳(1−s​i​m​(O​R​(j,N​O​T​(j)),T​r​u​e))+∑v∈𝒴(1−s​i​m​(O​R​(v,N​O​T​(v)),T​r​u​e))subscript𝑟6subscript𝑗𝒳1𝑠𝑖𝑚𝑂𝑅𝑗𝑁𝑂𝑇𝑗𝑇𝑟𝑢𝑒subscript𝑣𝒴1𝑠𝑖𝑚𝑂𝑅𝑣𝑁𝑂𝑇𝑣𝑇𝑟𝑢𝑒r\_{6}=\sum\_{j\in\mathcal{X}}\big{(}1-sim(OR(j,NOT(j)),True)\big{)}+\sum\_{v\in\mathcal{Y}}\big{(}1-sim(OR(v,NOT(v)),True)\big{)} |

Mapping an input job title j𝑗j to a normalized job title v𝑣v based solely on their similarity score is unwary. To alleviate uncertainty issues, it is necessary to also consider the similarity scores of j𝑗j with the rest of the normalized job titles in the set 𝒴𝒴\mathcal{Y}. For example, if the mapping score between j𝑗j and a certain vk∈𝒴subscript𝑣𝑘𝒴v\_{k}\in\mathcal{Y} is high at 0.990.990.99, while the mapping scores between j𝑗j and the other vl∈𝒴subscript𝑣𝑙𝒴v\_{l}\in\mathcal{Y} (l≠k𝑙𝑘l\neq k) are low at 0.010.010.01, then it is considered *certain* that j𝑗j maps to vksubscript𝑣𝑘v\_{k}. However, if the mapping score between j𝑗j and vk∈𝒴subscript𝑣𝑘𝒴v\_{k}\in\mathcal{Y} is high at 0.90.90.9, and the mapping scores between j𝑗j and a few other vl∈𝒴subscript𝑣𝑙𝒴v\_{l}\in\mathcal{Y} (l≠k𝑙𝑘l\neq k) are close to (j𝑗j, vksubscript𝑣𝑘v\_{k}), then there is high *uncertainty* when mapping j𝑗j to vksubscript𝑣𝑘v\_{k}, even though its mapping score is the highest. Therefore, we need a mechanism that takes into account mapping scores of j𝑗j with all vk∈𝒴subscript𝑣𝑘𝒴v\_{k}\in\mathcal{Y} simultaneously.

In other words, we need a mechanism that considers collaborative supports across all the mapping scores. Specifically, in the example above, the mapping decision can be made by a reasoning procedure that checks if j𝑗j is mostly similar to vksubscript𝑣𝑘v\_{k}, and totally dissimilar to the rest of the job titles vl∈𝒴subscript𝑣𝑙𝒴v\_{l}\in\mathcal{Y} (l≠k𝑙𝑘l\neq k), and concludes that j𝑗j maps to vksubscript𝑣𝑘v\_{k}. Such a reasoning procedure can be represented as a logical structure, leading us to use neural collaborative reasoning [[12](#bib.bib12)]. Furthermore, our ablation study demonstrates that the reasoning improves the performance of *JTN*. Thus, we can represent such a reasoning procedure as a logical structure, as shown below:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s​i​m​(ji,v1)∧s​i​m​(ji,v2)∧s​i​m​(ji,v3)→v3→𝑠𝑖𝑚subscript𝑗𝑖subscript𝑣1𝑠𝑖𝑚subscript𝑗𝑖subscript𝑣2𝑠𝑖𝑚subscript𝑗𝑖subscript𝑣3subscript𝑣3sim(j\_{i},v\_{1})\wedge sim(j\_{i},v\_{2})\wedge{sim}(j\_{i},v\_{3})\rightarrow v\_{3} |  | (7) |

Hence, we are inspired to design a neural collaborative reasoning module [[12](#bib.bib12)] that learns reasoning-based representations of the input job titles. In this sense, the problem of predicting v2subscript𝑣2v\_{2} as a correct mapping or not with the example above (i.e., Equation ([7](#S4.E7 "In IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning"))) is converted into the problem of deciding if the following Horn clause is True or False:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s​i​m​(ji,v1)∧s​i​m​(ji,v2)→s​i​m​(ji,v3)→𝑠𝑖𝑚subscript𝑗𝑖subscript𝑣1𝑠𝑖𝑚subscript𝑗𝑖subscript𝑣2𝑠𝑖𝑚subscript𝑗𝑖subscript𝑣3sim(j\_{i},v\_{1})\wedge sim(j\_{i},v\_{2})\rightarrow{sim}(j\_{i},v\_{3}) |  | (8) |

Note that due to the lack of topological information of normalized job titles, we are not able to produce topological embeddings for normalized job titles. However, producing semantic embeddings and syntactic embeddings for normalized job titles is straight-forward and follows a similar process as for input job titles. As such, we define a Horn clause for finding a mapping between the input job title jisubscript𝑗𝑖j\_{i} and a correct mapping standard job title vc∈𝒴subscript𝑣𝑐𝒴v\_{c}\in\mathcal{Y} with regard to the input semantic embeddings of both jisubscript𝑗𝑖j\_{i} and vksubscript𝑣𝑘v\_{k} can be defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s​i​m​(ji(b),v1(b))∧⋯∧s​i​m​(ji(b),v|𝒴|(b))→s​i​m​(ji(b),vc(b))→𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑏superscriptsubscript𝑣1𝑏⋯𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑏superscriptsubscript𝑣𝒴𝑏𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑏superscriptsubscript𝑣𝑐𝑏sim(j\_{i}^{(b)},v\_{1}^{(b)})\wedge\dots\wedge{sim}(j\_{i}^{(b)},v\_{|\mathcal{Y}|}^{(b)})\rightarrow{sim}(j\_{i}^{(b)},v\_{c}^{(b)}) |  | (9) |

Based on the De Morgan’s Law, we can re-write Equation ([9](#S4.E9 "In IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning")) using only two basic logical operator *OR* (i.e., ∨\vee) and *NOT* (i.e., ¬\neg) and obtain the reasoning-based representation 𝑿𝒃′subscriptsuperscript𝑿bold-′𝒃\boldsymbol{{X}^{\prime}\_{b}}\;of jisubscript𝑗𝑖j\_{i} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑿𝒃′=¬s​i​m​(ji(b),v1(b))∨⋯∨¬s​i​m​(ji(b),v|𝒴|(b))∨s​i​m​(ji(b),vc(b))subscriptsuperscript𝑿bold-′𝒃𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑏superscriptsubscript𝑣1𝑏⋯𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑏superscriptsubscript𝑣𝒴𝑏𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑏superscriptsubscript𝑣𝑐𝑏\boldsymbol{{X}^{\prime}\_{b}}=\neg sim(j\_{i}^{(b)},v\_{1}^{(b)})\vee\dots\vee\neg{sim}(j\_{i}^{(b)},v\_{|\mathcal{Y}|}^{(b)})\vee{sim}(j\_{i}^{(b)},v\_{c}^{(b)}) |  | (10) |

Similarly, we can obtain the reasoning-based representation 𝑿𝒔′subscriptsuperscript𝑿bold-′𝒔\boldsymbol{{X}^{\prime}\_{s}}\;of jisubscript𝑗𝑖j\_{i} with regard to the syntactic embedding view as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑿𝒔′=¬s​i​m​(ji(s),v1(s))∨⋯∨¬s​i​m​(ji(s),v|𝒴|(s))∨s​i​m​(ji(s),vc(s))subscriptsuperscript𝑿bold-′𝒔𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑠superscriptsubscript𝑣1𝑠⋯𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑠superscriptsubscript𝑣𝒴𝑠𝑠𝑖𝑚superscriptsubscript𝑗𝑖𝑠superscriptsubscript𝑣𝑐𝑠\boldsymbol{{X}^{\prime}\_{s}}=\neg sim(j\_{i}^{(s)},v\_{1}^{(s)})\vee\dots\vee\neg{sim}(j\_{i}^{(s)},v\_{|\mathcal{Y}|}^{(s)})\vee{sim}(j\_{i}^{(s)},v\_{c}^{(s)}) |  | (11) |

![Refer to caption](/html/2202.10739/assets/Figs/reasoning.png)

Figure 9: Architecture for reasoning-based representation.

Figure [9](#S4.F9 "Figure 9 ‣ IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") summarizes our architecture for the neural logical reasoning.
With reasoning-based representations 𝑿𝒃′subscriptsuperscript𝑿bold-′𝒃\boldsymbol{{X}^{\prime}\_{b}}\;and 𝑿𝒔′subscriptsuperscript𝑿bold-′𝒔\boldsymbol{{X}^{\prime}\_{s}}\;are now established together in Equation ([10](#S4.E10 "In IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning")) and ([11](#S4.E11 "In IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning")), as well as co-attentive multi-aspect embeddings 𝑿^𝒉subscriptbold-^𝑿𝒉\boldsymbol{\hat{X}\_{h}}\;, 𝑿^𝒃subscriptbold-^𝑿𝒃\boldsymbol{\hat{X}\_{b}}\;, and 𝑿^𝒔subscriptbold-^𝑿𝒔\boldsymbol{\hat{X}\_{s}}\;(Equation ([6](#S4.E6 "In IV-B Multi-Aspect Co-Attention ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning"))), we next fuse these embeddings to have a final representation of the input job title.

### IV-D Fusion

We concatenate the reasoning-based representations 𝑿𝒃′subscriptsuperscript𝑿bold-′𝒃\boldsymbol{{X}^{\prime}\_{b}}\;and 𝑿𝒔′subscriptsuperscript𝑿bold-′𝒔\boldsymbol{{X}^{\prime}\_{s}}\;, and the co-attentive multi-aspect embeddings 𝑿^𝒉subscriptbold-^𝑿𝒉\boldsymbol{\hat{X}\_{h}}\;, 𝑿^𝒃subscriptbold-^𝑿𝒃\boldsymbol{\hat{X}\_{b}}\;, and 𝑿^𝒔subscriptbold-^𝑿𝒔\boldsymbol{\hat{X}\_{s}}\;. Then we project the final job title embeddings into the size of all standard job titles |𝒴|𝒴|\mathcal{Y}| and generate a class probability distribution through the softmax operator.

|  |  |  |  |
| --- | --- | --- | --- |
|  | y^=softmax(ReLU(W(\hat{y}=softmax(ReLU(W( [𝑿^𝒉subscriptbold-^𝑿𝒉\boldsymbol{\hat{X}\_{h}}\;; 𝑿^𝒃subscriptbold-^𝑿𝒃\boldsymbol{\hat{X}\_{b}}\;; 𝑿^𝒔subscriptbold-^𝑿𝒔\boldsymbol{\hat{X}\_{s}}\;; 𝑿𝒃′subscriptsuperscript𝑿bold-′𝒃\boldsymbol{{X}^{\prime}\_{b}}\;; 𝑿𝒔′subscriptsuperscript𝑿bold-′𝒔\boldsymbol{{X}^{\prime}\_{s}}\;] )))))) |  | (12) |

### IV-E Learning Objective

We use the categorical cross-entropy as the loss function to train our JAMES. The categorical cross-entropy loss function is defined as following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ)=−∑j∈𝒴yj​l​o​g​(y^j)𝐿𝜃subscript𝑗𝒴subscript𝑦𝑗𝑙𝑜𝑔subscript^𝑦𝑗L(\theta)=-\sum\_{j\in{\mathcal{Y}}}y\_{j}log(\hat{y}\_{j}) |  | (13) |

where θ𝜃\theta
refers to all the parameters in the entire model.

In our implementation for reasoning-based representaion (Equation ([10](#S4.E10 "In IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning")) and ([11](#S4.E11 "In IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning"))), following [[12](#bib.bib12)], the OR module is implemented by a multi-layer perceptron (MLP) with one hidden layer, and the NOT/NEGATION module is also implemented by another multi-layer perceptron. To explicitly guarantee that these OR and NOT modules implement the expected logic operations, we constraints them with logical regularization as defined in Table [III](#S4.T3 "TABLE III ‣ IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning"). The final loss function of our JAMES is defined as followings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ)=−∑j∈𝒴yj​l​o​g​(y^j)+∑q=16rq𝐿𝜃subscript𝑗𝒴subscript𝑦𝑗𝑙𝑜𝑔subscript^𝑦𝑗subscriptsuperscript6𝑞1subscript𝑟𝑞L(\theta)=-\sum\_{j\in{\mathcal{Y}}}y\_{j}log(\hat{y}\_{j})+\sum^{6}\_{q=1}{r\_{q}} |  | (14) |

where ∑q=16rqsubscriptsuperscript6𝑞1subscript𝑟𝑞\sum^{6}\_{q=1}{r\_{q}} is the summation of all six neural logical regularizations that are defined in Table [III](#S4.T3 "TABLE III ‣ IV-C Reasoning-based Representations ‣ IV Our Proposed Model: JAMES ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning").

## V Empirical Validation

In this section, we present the evaluation results of our proposed JAMES model against competing baselines. We use our large-scale *JTN* dataset for the comparison, as other *JTN* datasets from [[6](#bib.bib6), [7](#bib.bib7), [23](#bib.bib23)] are not publicly available. We attempt to answer the following Evaluation Questions (EQ):

* ∙∙\bullet

  EQ1: How does JAMES perform against the baselines?
* ∙∙\bullet

  EQ2: Which components in JAMES are more helpful?
* ∙∙\bullet

  EQ3: Can JAMES be useful for other downstream tasks?

### V-A Experimental Settings

#### V-A1 Baselines

We compare JAMES against an exhaustive list of ten baseline models, including traditional simple solutions and state-of-the-art models: KNN-based [[16](#bib.bib16)], Word2Vec-based [[28](#bib.bib28)], DeepCarotene [[15](#bib.bib15)], Node2Vec [[29](#bib.bib29)], GloVe [[30](#bib.bib30)], NEO [[13](#bib.bib13)], WoLMIS [[14](#bib.bib14)], SBERT [[31](#bib.bib31)], Job2Vec [[18](#bib.bib18)], and Universal Sentence Encoder (USE) [[32](#bib.bib32)].
Note that as job descriptions are not available in our dataset, we construct the baseline models using only job titles to enable a fair comparison.

#### V-A2 Evaluation protocols

To evaluate the performance of all compared models, we use two widely used ranking metrics, *Precision*@N and *NDCG*@N, with N𝑁N being the top-N𝑁N results produced by each model. *Precision*@N accounts for the number of relevant results among top-N𝑁N output candidates, while *NDCG*@N applies an increasing discount of *log2* to items at lower ranks. We divide the dataset into 64%, 16%, and 20%, where we train for 64% using 16% as a validation, and then test for 20% for the *JTN* task.
Regarding our implementation settings, we use their reported hyperparameter settings for baseline models. For the GloVe-based (word-based) models, the dimension is set to 300.
For the Universal Sentence Encoder (USE), we use 512 dimensions, which is the default setting by the provider, and the SBERT’s embedding size is set to 768 for the same reason. For Node2Vec, we choose 128 accounting for execution time on a large-scale graph dataset. For our model, we vary the embedding size from {128, 256, 512}. During training, the number of epochs is set to 200 with early stopping. Our model and all the baselines are trained with a batch size of 256 using the Adam optimizer and learning rate of 10−3superscript10310^{-3}.

TABLE IV: Precision@10 and NDCG@10 of JAMES and baseline models on our dataset. The best results are in bold, the best baseline’s performance is underlined.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Model | Venue | Precision@10 | NDCG@10 |
| (i) | KNN-based [[16](#bib.bib16)] | CoRR’16 | 0.0913 | 0.0871 |
| (ii) | Word2Vec-based [[28](#bib.bib28)] | ECML’17 | 0.1254 | 0.0544 |
| (iii) | DeepCarotene [[15](#bib.bib15)] | BigData’19 | 0.1255 | 0.0543 |
| (iv) | Node2Vec [[29](#bib.bib29)] | KDD’16 | 0.1255 | 0.0609 |
| (v) | GloVe [[30](#bib.bib30)] | EMNLP’14 | 0.3080 | 0.1817 |
| (vi) | NEO [[13](#bib.bib13)] | ISWC’20 | 0.3422 | 0.2054 |
| (vii) | WoLMIS [[14](#bib.bib14)] | IIS’18 | 0.3536 | 0.2480 |
| (viii) | SBERT [[31](#bib.bib31)] | EMNLP’19 | 0.6121 | 0.4720 |
| (ix) | Job2Vec [[18](#bib.bib18)] | CIKM’19 | 0.6122 | 0.4622 |
| (x) | USE [[32](#bib.bib32)] | EMNLP’18 | 0.6619 | 0.4887 |
|  | JAMES | Ours | 0.7285 | 0.5743 |

### V-B EQ1: Performance of JAMES

Table [IV](#S5.T4 "TABLE IV ‣ V-A2 Evaluation protocols ‣ V-A Experimental Settings ‣ V Empirical Validation ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") shows the overall performance of JAMES and the compared models on our large-scale *JTN* dataset. We observe that word-based baselines (baseline (i, ii, iii)) perform the worst. This can be attributed to two main reasons. First, word-level baselines mostly rely on word embedding techniques and do not account for contextual word semantic relationships in job titles, which results in a failure to mitigate the interdisciplinary correlation among job titles. Second, the word-level semantic baselines use additional job descriptions to enhance their performance, but job descriptions are not always publicly available in *JTN* datasets, have limited access, and are expensive to collect. Although baseline (v) performs better than the word-based baselines, its performance is still significantly lower than other models. JAMES significantly outperforms Node2Vec (baseline (iv)), indicating that using only graph representation learning is suboptimal.

Models that are more applied and job-specific (baseline (vi, vii)) achieve higher performance compared to word-level semantic models and topological baseline, as they are able to deal with both messy and interdisciplinary job titles, though JAMES still outperforms them. The sentence-level semantic-based models (baseline (viii, ix, x)) perform very well in contrast to other baselines because they can extract and represent semantic meanings using pretrained models.

In short, JAMES vastly outperforms all related baselines by utilizing our multi-aspect co-attentive reasoning representation. An important reason for this is that all prior models were developed using *company-generated* “pure” job titles, while our dataset is *user-generated* “impure” job titles. Compared to the best baseline, i.e., USE, JAMES improves *Precision@10* by 10.06% and *NDCG@10* by 17.52%, confirming the effectiveness of JAMES.

### V-C EQ2: Ablation Study

We conducted an ablation study to address EQ2. Since SBERT (i.e., baselines viii  and x) yielded relatively good performance and BERT embedding is an essential feature of our model, we evaluated the performance of removing each single component of JAMES except for the BERT embedding. Table [V](#S5.T5 "TABLE V ‣ V-C EQ2: Ablation Study ‣ V Empirical Validation ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") presents the results. We observed two main findings.
First, hyperbolic graph embeddings have a significant contribution to the *JTN* performance of JAMES. Removing this component from JAMES without co-attention and reasoning led to a reduction of *Precision@10* by 18.28% and *NDCG@10* by 19.62%. This demonstrates the effectiveness of hyperbolic graph embeddings for the major issues in *JTN* task, such as overlapping and messy job titles (i.e., Challenge 1-3 in Introduction).
Second, co-attention (CoAtt) and reasoning-based representation (Reasoning) improved the performance from the simple concatenation model by 4.70% in *Precision@10* and 7.47% in *NDCG@10*, showing the effectiveness of multi-aspect co-attention and fusion of co-attentive multi-aspect embeddings and reasoning-based representations. In summary, the removal of each component in JAMES reduced its performance, indicating the effectiveness of our model.

TABLE V:
Ablation study experiments for JAMES.

|  |  |  |
| --- | --- | --- |
| Model | Precision@10 | NDCG@10 |
| JAMES | 0.7285 | 0.5743 |
| - CoAtt (=αabsent𝛼=\alpha) | 0.6996 (↓↓\downarrow 4.13%) | 0.5630 (↓↓\downarrow 2.01%) |
| - α𝛼\alpha - Reasoning (=βabsent𝛽=\beta) | 0.6958 (↓↓\downarrow 4.70%) | 0.5344 (↓↓\downarrow 7.47%) |
| - β𝛽\beta - Syntactic | 0.6273 (↓↓\downarrow 16.13%) | 0.4859 (↓↓\downarrow 18.19%) |
| - β𝛽\beta - Hyperbolic Graph (=κabsent𝜅=\kappa) | 0.6159 (↓↓\downarrow 18.28%) | 0.4801 (↓↓\downarrow 19.62%) |
| - κ𝜅\kappa - Syntactic | 0.6121 (↓↓\downarrow 19.02%) | 0.4720 (↓↓\downarrow 21.67%) |

### V-D EQ3: Other Downstream Tasks

To assess the performance of JAMES in other job-domain downstream tasks, we conducted additional experiments as follows.

#### V-D1 Link Prediction

Link prediction is one of the most common tasks for graphs and networks [[33](#bib.bib33), [34](#bib.bib34), [35](#bib.bib35)]. In this part, to see the effectiveness of the multi-aspect embeddings learned by JAMES, we present an additional capability of JAMES in the link prediction task. We compare JAMES with Node2Vec, Word2Vec, GloVe, USE, and Job2Vec as representative baselines.

To generate the training/development/testing sets for the link prediction task, we randomly removed 20% of the total number of links in the graph, considering them as the positive links in the testing set, and sampled the same amount of negative links in the graph for the testing set. We also randomly removed 20% of the positive links in the remaining 80% positive links and sampled the same amount of negative links to form a development set. The rest of the graph was kept as a training set. Then, we followed [[29](#bib.bib29)] and used different binary operators (i.e., Average, Hadmard, Weighted-L1, and Weighted-L2) to obtain the link embedding from the employee node embedding, the job-title node embedding obtained by JAMES, and the link/edge that connects these two nodes. We selected the best binary operator using the development set and reported the performance metric using AUC.

Table [VI](#S5.T6 "TABLE VI ‣ V-D1 Link Prediction ‣ V-D EQ3: Other Downstream Tasks ‣ V Empirical Validation ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") shows the performance of JAMES and the compared methods. The best baseline is Job2Vec, and we observe that JAMES outperforms all of the baselines. Specifically, JAMES relatively improves Job2Vec by 5.59% of AUC. This result demonstrates that the multi-aspect embeddings from our JAMES model are effective not only for *JTN* task but also for link prediction.

TABLE VI: AUC in link prediction task.

|  |  |
| --- | --- |
| Method | AUC |
| Word2Vec-based [[28](#bib.bib28)] | 0.5648 |
| GloVe [[30](#bib.bib30)] | 0.6278 |
| USE [[32](#bib.bib32)] | 0.8370 |
| Node2Vec [[29](#bib.bib29)] | 0.8743 |
| Job2Vec [[18](#bib.bib18)] | 0.9431 |
| JAMES | 0.9957 |

TABLE VII: Job Mobility Prediction

|  |  |
| --- | --- |
| Method | MAP@10 |
| No *JTN* (unpreprocessed) + NEMO [[23](#bib.bib23)] | 0.5349 |
| Job2Vec [[18](#bib.bib18)] + NEMO [[23](#bib.bib23)] | 0.6418 |
| USE [[32](#bib.bib32)] + NEMO [[23](#bib.bib23)] | 0.6529 |
| JAMES + NEMO [[23](#bib.bib23)] | 0.7013 |

#### V-D2 Job Mobility Prediction.

Job mobility prediction is an essential job-domain downstream task [[23](#bib.bib23), [3](#bib.bib3), [36](#bib.bib36), [37](#bib.bib37)]. It involves predicting a user’s next job titles based on their sequence of job trajectories, wherein *JTN* is conducted for preprocessing the dataset.
Specifically, we use JAMES to preprocess our resume dataset, by converting each input job title with the *top-1* matching standard job title. To compare with our JAMES, we use Job2Vec, USE as baselines. We also prepare the unpreprocessed dataset.
For the job mobility prediction model, we adopt NEMO [[23](#bib.bib23)] as it is the state-of-the-art model, and evaluate its performance using mean average precision at 10 (MAP@10) as the metric. Note that we only consider the job title transition information for our evaluation, as other features are costly to collect and are not available in our dataset. We compare the impact of the *JTN* methods on the model’s performance.

Table [VII](#S5.T7 "TABLE VII ‣ V-D1 Link Prediction ‣ V-D EQ3: Other Downstream Tasks ‣ V Empirical Validation ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") shows the performance of the job mobility prediction task using the JAMES and baselines for preprocessing. The results demonstrate that the JAMES has a considerable impact on the job mobility prediction model’s performance. Its multifaceted mapping approach assists job mobility prediction models in learning more effectively, resulting in a performance improvement. Although the accuracy improvement alone does not provide insights into user behavior, the effectiveness of JAMES in improving performance suggests its potential applicability in various job-domain downstream tasks.

## VI JAMES API and Use Cases

To make JAMES accessible as a public resource, we release a RESTful API for JAMES. This API allows users to input any textual job title entity and receive the corresponding normalized job titles based on the public taxonomy (i.e., ESCO). Users are able to obtain up to the top-5 most relevant normalized job titles, which helps individuals or organizations in preprocessing and cleansing their job title datasets for job-domain downstream tasks. The API provides the output predicted by JAMES if the input job entity is included in our graph. Otherwise, the API employs textual embeddings to get the output so that users can use any text and retrieve relevant normalized job titles.
We also built a demo website that users can touch and see the results more intuitively. Figure [10](#S6.F10 "Figure 10 ‣ VI JAMES API and Use Cases ‣ JAMES: Normalizing Job Titles with Multi-Aspect Graph Embeddings and Reasoning") shows the screenshot of JAMES web app that uses our API behind.

Our JAMES API has the potential for a wide range of applications and use cases, as listed below:

* •

  *Recruitment platforms*: By integrating job titles, JAMES API enables recruiters and job seekers to more easily compare job titles and requirements across different companies and industries.
* •

  *Resume standardization*: JAMES API can be incorporated to automatically normalize job titles in users-uploaded resumes on online platforms, facilitating the matchmaking between job seekers with job postings.
* •

  *Market research*: JAMES API is also beneficial in market and economic research for tracking job trends and analyzing job requirements across different industries and regions, as economic researchers typically need to clean job titles for their analysis.
* •

  *Search query expansion*: By mapping all variations of an entity to a single normalized form, JAMES API can be used to improve the relevance of job search results, expanding the search to include all documents that mention the normalized job titles.

![Refer to caption](/html/2202.10739/assets/Figs/API_page2.png)

Figure 10: JAMES API demo page. This shows an example of the job title normalization for “taxi driver”

## VII Conclusion

In this paper, we proposed a novel job title normalization model, JAMES, toward creating a fine-grained job taxonomy using a real-world and large-scale career trajectory dataset. Our approach utilized multi-aspect embeddings (i.e., graph, semantic, and syntactic embedding), multi-aspect co-attention, and reasoning-based representation to address the challenges of the *Job Title Normalization* (*JTN*) task effectively.
We conducted extensive experiments comparing JAMES to ten baseline models on the *JTN* task and performed an ablation study. Furthermore, we conducted additional experiments on practical downstream tasks, such as link prediction and job mobility prediction, to assess the practical impact of our approach. Our results showed that: (1) JAMES outperformed all baseline models in the *JTN* task, and (2) JAMES was effective in job-domain downstream tasks. Finally, we release JAMES as an API for public use, which is useful for job-domain downstream tasks.

## Acknowledgment

This work was in part supported by NSF awards #1934782 and #1909702, and PSU CSRAI seed grant 2021.

## References

* [1]

  K. Kenthapadi, B. Le, and G. Venkataraman, “Personalized job recommendation
  system at linkedin: Practical challenges and lessons learned,” in
  *Proceedings of the ACM conference on recommender systems (RecSys)*,
  2017, pp. 346–347.
* [2]

  I. Paparrizos, B. B. Cambazoglu, and A. Gionis, “Machine learned job
  recommendation,” in *Proceedings of the ACM conference on recommender
  systems (RecSys)*, 2011, pp. 325–328.
* [3]

  Q. Meng, H. Zhu, K. Xiao, L. Zhang, and H. Xiong, “A hierarchical
  career-path-aware neural network for job mobility prediction,” in
  *Proceedings of the International ACM SIGKDD Conference on Knowledge
  Discovery and Data Mining (KDD)*, 2019, pp. 14–24.
* [4]

  H. Xu, Z. Yu, J. Yang, H. Xiong, and H. Zhu, “Dynamic talent flow analysis
  with deep sequence prediction modeling,” *IEEE Transactions on
  Knowledge and Data Engineering (TKDE)*, vol. 31, no. 10, pp. 1926–1939,
  2018.
* [5]

  H. Li, Y. Ge, H. Zhu, H. Xiong, and H. Zhao, “Prospecting the career
  development of talents: A survival analysis perspective,” in
  *Proceedings of the International ACM SIGKDD Conference on Knowledge
  Discovery and Data Mining (KDD)*, 2017, pp. 917–925.
* [6]

  L. Zhang, T. Xu, H. Zhu, C. Qin, Q. Meng, H. Xiong, and E. Chen, “Large-scale
  talent flow embedding for company competitive analysis,” in
  *Proceedings of the Web Conference (WWW)*, 2020, pp. 2354–2364.
* [7]

  V. S. Dave, B. Zhang, M. Al Hasan, K. AlJadda, and M. Korayem, “A combined
  representation learning approach for better job and skill recommendation,”
  in *Proceedings of the ACM International Conference on Information and
  Knowledge Management (CIKM)*, 2018, pp. 1997–2005.
* [8]

  S. Li, B. Shi, J. Yang, J. Yan, S. Wang, F. Chen, and Q. He, “Deep job
  understanding at linkedin,” in *Proceedings of the International ACM
  SIGIR Conference on Research and Development in Information Retrieval
  (SIGIR)*, 2020, pp. 2145–2148.
* [9]

  M. Nickel and D. Kiela, “Poincaré embeddings for learning hierarchical
  representations,” 2017, pp. 6341–6350.
* [10]

  O.-E. Ganea, G. Bécigneul, and T. Hofmann, “Hyperbolic neural networks,”
  2018, pp. 5350–5360.
* [11]

  I. Chami, R. Ying, C. Ré, and J. Leskovec, “Hyperbolic graph convolutional
  neural networks,” *Advances in Neural Information Processing Systems
  (NeurIPS)*, vol. 32, p. 4869, 2019.
* [12]

  H. Chen, S. Shi, Y. Li, and Y. Zhang, “Neural collaborative reasoning,” in
  *Proceedings of the Web Conference (WWW)*, 2021, pp. 1516–1527.
* [13]

  A. Giabelli, L. Malandri, F. Mercorio, M. Mezzanzanica, and A. Seveso, “Neo: A
  tool for taxonomy enrichment with new emerging occupations,” in
  *International Semantic Web Conference*.   Springer, 2020, pp. 568–584.
* [14]

  R. Boselli, M. Cesarini, S. Marrara, F. Mercorio, M. Mezzanzanica, G. Pasi, and
  M. Viviani, “Wolmis: a labor market intelligence system for classifying web
  job vacancies,” *Journal of Intelligent Information Systems*, vol. 51,
  no. 3, pp. 477–502, 2018.
* [15]

  J. Wang, K. Abdelfatah, M. Korayem, and J. Balaji, “Deepcarotene-job title
  classification with multi-stream convolutional neural network,” in
  *2019 IEEE International Conference on Big Data (Big Data)*.   IEEE, 2019, pp. 1953–1961.
* [16]

  Y. Zhu, F. Javed, and O. Ozturk, “Semantic similarity strategies for job title
  classification,” *CoRR*, vol. abs/1609.06268, 2016. [Online].
  Available: http://arxiv.org/abs/1609.06268
* [17]

  H. Luo, S. Ma, A. J. B. Selvaraj, and Y. Sun, “Learning job representation
  using directed graph embedding,” in *Proceedings of the International
  Workshop on Deep Learning Practice for High-Dimensional Sparse Data*, 2019,
  pp. 1–5.
* [18]

  D. Zhang, J. Liu, H. Zhu, Y. Liu, L. Wang, P. Wang, and H. Xiong, “Job2vec:
  Job title benchmarking with collective multi-view representation learning,”
  in *Proceedings of the ACM International Conference on Information and
  Knowledge Management (CIKM)*, 2019, pp. 2763–2771.
* [19]

  Y. Liu, L. Zhang, L. Nie, Y. Yan, and D. Rosenblum, “Fortune teller:
  predicting your career path,” in *Proceedings of the AAAI Conference on
  Artificial Intelligence (AAAI)*, vol. 30, no. 1, 2016.
* [20]

  B. Shi, J. Yang, F. Guo, and Q. He, “Salience and market-aware skill
  extraction for job targeting,” in *Proceedings of the International ACM
  SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)*, 2020, pp.
  2871–2879.
* [21]

  C. Qin, H. Zhu, T. Xu, C. Zhu, L. Jiang, E. Chen, and H. Xiong, “Enhancing
  person-job fit for talent recruitment: An ability-aware neural network
  approach,” in *Proceedings of the International ACM SIGIR Conference on
  Research and Development in Information Retrieval (SIGIR)*, 2018, pp. 25–34.
* [22]

  M. Yamashita, Y. Li, T. Tran, Y. Zhang, and D. Lee, “Looking further into the
  future: Career pathway prediction,” *ACM WSDM Workshop on Computational
  Jobs Marketplace 2022*, 2022.
* [23]

  L. Li, H. Jing, H. Tong, J. Yang, Q. He, and B.-C. Chen, “Nemo: Next career
  move prediction with contextual embedding,” in *Proceedings of the
  International Conference on World Wide Web Companion*, 2017, pp. 505–513.
* [24]

  J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep
  bidirectional transformers for language understanding,” *arXiv preprint
  arXiv:1810.04805*, 2018.
* [25]

  N. Reimers and I. Gurevych, “Sentence-bert: Sentence embeddings using siamese
  bert-networks,” in *Proceedings of the Conference on Empirical Methods
  in Natural Language Processing and the International Joint Conference on
  Natural Language Processing (EMNLP-IJCNLP)*, 2019, pp. 3982–3992.
* [26]

  Z. Yang, D. Yang, C. Dyer, X. He, A. Smola, and E. Hovy, “Hierarchical
  attention networks for document classification,” in *Proceedings of the
  Conference of the North American chapter of the Association for Computational
  Linguistics: Human Language Technologies (NAACL)*, 2016, pp. 1480–1489.
* [27]

  J. Lu, J. Yang, D. Batra, and D. Parikh, “Hierarchical question-image
  co-attention for visual question answering,” *Advances in Neural
  Information Processing Systems (NeurIPS)*, vol. 29, pp. 289–297, 2016.
* [28]

  R. Boselli, M. Cesarini, F. Mercorio, and M. Mezzanzanica, “Using machine
  learning for labour market intelligence,” in *Joint European Conference
  on Machine Learning and Knowledge Discovery in Databases*.   Springer, 2017, pp. 330–342.
* [29]

  A. Grover and J. Leskovec, “node2vec: Scalable feature learning for
  networks,” in *Proceedings of the International ACM SIGKDD Conference
  on Knowledge Discovery and Data Mining (KDD)*, 2016, pp. 855–864.
* [30]

  J. Pennington, R. Socher, and C. D. Manning, “Glove: Global vectors for word
  representation,” in *Proceedings of the Conference on Empirical Methods
  in Natural Language Processing (EMNLP)*, 2014, pp. 1532–1543.
* [31]

  N. Reimers and I. Gurevych, “Sentence-bert: Sentence embeddings using siamese
  bert-networks,” in *Proceedings of the Conference on Empirical Methods
  in Natural Language Processing and the International Joint Conference on
  Natural Language Processing (EMNLP-IJCNLP)*, 2019, pp. 3982–3992.
* [32]

  D. Cer, Y. Yang, S.-y. Kong, N. Hua, N. Limtiaco, R. S. John, N. Constant,
  M. Guajardo-Cespedes, S. Yuan, C. Tar *et al.*, “Universal sentence
  encoder for english,” in *Proceedings of the Conference on Empirical
  Methods in Natural Language Processing: System Demonstrations*, 2018, pp.
  169–174.
* [33]

  A. Kumar, S. S. Singh, K. Singh, and B. Biswas, “Link prediction techniques,
  applications, and performance: A survey,” *Physica A: Statistical
  Mechanics and its Applications*, vol. 553, p. 124289, 2020.
* [34]

  L. Cai and S. Ji, “A multi-scale approach for graph link prediction,” in
  *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)*,
  vol. 34, no. 04, 2020, pp. 3308–3315.
* [35]

  M. Zhang and Y. Chen, “Link prediction based on graph neural networks,”
  *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 31,
  pp. 5165–5175, 2018.
* [36]

  L. Zhang, D. Zhou, H. Zhu, T. Xu, R. Zha, E. Chen, and H. Xiong, “Attentive
  heterogeneous graph embedding for job mobility prediction,” in
  *Proceedings of the International ACM SIGKDD Conference on Knowledge
  Discovery and Data Mining (KDD)*, 2021, pp. 2192–2201.
* [37]

  C. Wang, H. Zhu, Q. Hao, K. Xiao, and H. Xiong, “Variable interval time
  sequence modeling for career trajectory prediction: Deep collaborative
  perspective,” in *Proceedings of The ACM Web Conference (WWW)*, 2021,
  pp. 612–623.

[◄](/html/2202.10738)
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling
lucky?](/feeling_lucky)

[Conversion
report](/log/2202.10739)
[Report
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2202.10739)
[View original
on arXiv](https://arxiv.org/abs/2202.10739)[►](/html/2202.10740)
