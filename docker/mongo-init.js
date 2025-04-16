// mongo-init.js - MongoDB initialization script for Red Corps AI Sentinel

const now = new Date();
const oneYearLater = new Date();
oneYearLater.setFullYear(now.getFullYear() + 1);

// Switch to target DB
const dbName = "sentinel";
db = db.getSiblingDB(dbName);

// Create collections
print("📁 Creating collections...");
db.createCollection("scans");
db.createCollection("licenses");

// Insert test license document
db.licenses.insertOne({
  client_id: "test-client",
  plan: "Pro",
  issued: now,
  expires: oneYearLater,
  features: ["ai_risk_scoring", "report_export", "compliance_mapper"],
  activated: true,
  notes: "Default testing license seeded by mongo-init.js"
});

print(`✅ MongoDB initialized with database '${dbName}' and seeded collections.`);
