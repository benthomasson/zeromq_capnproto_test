@0xadd0fc6f3dae89b8;

struct CPU {
  cpu @0 :Float32;
}

struct Memory {
  total @0 :UInt64;
  available @1 :UInt64;
  used @2 :UInt64;
  free @3 :UInt64;
  active @4 :UInt64;
  wired @5 :UInt64;
  inactive @6 :UInt64;
  percent @7 :Float32;
}


struct Measurements {
  id @0 :UInt64;
  timestamp @1 :Text;
  cpu @2 :CPU;
  memory @3 :Memory;
}
