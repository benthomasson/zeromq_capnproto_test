@0xadd0fc6f3dae89b8;

struct CPU {
  id @0 :UInt32;
  cpu @1 :Float32;
}

struct Memory {
  id @0 :UInt32;
  total @1 :UInt64;
  available @2 :UInt64;
  used @3 :UInt64;
  free @4 :UInt64;
  active @5 :UInt64;
  wired @6 :UInt64;
  inactive @7 :UInt64;
  percent @8 :Float32;
}


struct Measurements {
  cpu @0 :CPU;
  memory @1 :Memory;
}
