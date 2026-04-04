import { openDB } from "idb";

export async function getDB() {
  return openDB("baccarat-db", 1, {
    upgrade(db) {
      db.createObjectStore("history", { keyPath: "id", autoIncrement: true });
    },
  });
}

export async function addRecord(record: any) {
  const db = await getDB();
  await db.put("history", record);
}

export async function getRecords(limit = 40) {
  const db = await getDB();
  const all = await db.getAll("history");
  return all.slice(-limit);
}

