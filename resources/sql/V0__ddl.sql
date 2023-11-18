CREATE TABLE "campaign_performance" (
   campaign_id TEXT NOT NULL,
   segment_id INTEGER NOT NULL,
   users INTEGER NOT NULL,
   PRIMARY KEY(campaign_id, segment_id)
);

CREATE TABLE "impressions" (
   id SERIAL,
   segment_id INTEGER NOT NULL,
   user_id INTEGER NOT NULL,
   ts TIMESTAMP,
   PRIMARY KEY(id)
);
