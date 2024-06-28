# Introduction
The database records the important data of the application and is a part of the pipeline
of collecting information from mass input source and prepare for possible high performance
computation for analysis and data mining.

The database is composed of four major tables:
- `userdata` and `apikeys` are maintaining user identification and access control
- `conversationdata` and `commentdata` are the key data we want to collect
  - `conversationdata` is the configuration of a conversation led by a user to collect comments
  - `commentdata` is the records of comments posted to a conversation

> At the heart of Polis is the idea that decisions should be made
> through open and transparent dialogue. `Conversation` in Polis refers to the structured process of:
> - Discussion and Debate: The community engages in a public discussion around the topic
> given by `conversation`. `Comments` in `conversations` is providing feedback:
> Sharing opinions and perspectives.
> - Voting: The community votes on the `comments` in `conversation` to show what direction would be
> favored by people and what direction would not.

We will have a deep dive in the technology used in database and detail of each table

# Database
## Overview
Database Type: StarRocks, data lake, support SQL

![](https://github.com/NewJerseyStyle/LitePolis/blob/release/doc/db-light.png?raw=true)

The database talbes and columns. [DBML available as reference](db.dbml)

> ℹ️ Consider `commentdata` as the fact table in Star schema,
> so the `userdata` and `conversationdata` are the dimension tables.

## Schema
### `userdata`
Information of users, serving as the identifier for comment creators who join a conversation.

> ⚠️ The table will deprecate after beta version release migrating to OpenID solution with OIDC server
> The `ID` and `EMAIL` columns will be used to identify users before they register,
> and the `EMAIL` column will be used for push notifications even after migrating to OpenID.
 
|Column|Data type|Description|
|:-----|:-------:|:----------|
|ID    |INT      |`primary_key`, auto-incrementing, unique identifier of a user|
|EMAIL |TEXT     |Contact information for push notifications|
|PASSWORD|TEXT   |SHA-1 hash of md5(password) where md5 hash is done on client side|
|PRIVILEGE| TEXT |User privilege level, default: "user", "root" only used during initialization, "moderator" is reserved for moderation in conversations|

### `conversationdata`
Stores information about conversations.
Table contains metadata about conversations, including the names, descriptions, and creators.

`Conversation` in Polis refers to the structured process mentioned in introduction.
You can also learn more in [pol.is](pol.is)

|Column|Data type|Description|
|:-----|:-------:|:----------|
|ID    |INT      |`primary_key`, auto-incrementing, unique identifier of a conversation|
|NAME  |TEXT     |Name of the conversation, required|
|DESCRIPTION|TEXT|Description of the conversation, optional|
|CREATOR_ID|INT  |Foreign key referencing the `ID` column in `userdata`, identifies the user who created the conversation|

### `commentdata`
Stores information about comments made in conversations.
Table contains metadata about comments, including their content, creation date,
and relationships to users and conversations.

|Column|Data type|Description|
|:-----|:-------:|:----------|
|ID    |INT      |`primary_key`, auto-incrementing, unique identifier of a comment|
|CREATE_DATE|DATETIME|Timestamp when the comment was created|
|COMMENT|TEXT    |Content of the comment, required|
|USER_ID|INT     |Foreign key referencing the `ID` column in `userdata`, identifies the user who made the comment, required|
|CONVERSATION_ID|INT|Foreign key referencing the `ID` column in `conversationdata`, identifies the conversation where the comment was made, required|
|MODERATED|BOOLEAN|Indicates whether the comment has been moderated, default: FALSE|
|APPROVED|BOOLEAN|Indicates whether the comment has been approved, default: FALSE|

### `apikeys`
Stores API keys for users.
Table contains API keys issued to users, allowing them to access the API.

|Column|Data type|Description|
|:-----|:-------:|:----------|
|API_KEY|TEXT    |`primary_key`, unique API key, required|
|USER_ID|INT     |Foreign key referencing the `ID` column in `userdata`, identifies the user who owns the API key, required|

## Future work
The table `userdata` will not be used for login after beta version release.
Login and access control will then relay on OpenID solution with OIDC server.

# Scalability and Availability
StarRocks is designed for high scalability and availability to handle increasing data volume and user traffic.

- Distributed architecture: You can add more nodes to the cluster to increase storage capacity and processing power.
- Data replication: StarRocks replicates data across multiple nodes, ensuring data availability even if a node fails.
- Elastic fault tolerance: StarRocks automatically detects and recovers from node failures, ensuring continuous operation.
- Real-time data analytics: StarRocks supports real-time data ingestion and analytics, allowing you to analyze data as it arrives.
