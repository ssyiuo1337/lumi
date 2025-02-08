export interface Subscription {
    sub_dur: number;
    start_date: string | null;
    expiration_date: string | null;
  }
  
  export interface Statistics {
    launch_number: number;
    playtime: string;
    last_launch: string;
    reg_date: string;
  }
  
  export interface RefferalSystem {
    refferal_available: boolean;
    code: string | null;
    refferal_number: number | null;
    refferal_bonus: number | null;
  }
  
  export interface User {
    id: number;
    username: string;
    private: boolean;
    email?: string;
    hwid?: string | null;
    role: string;
    subscription?: Subscription;
    statistics?: Statistics;
    refferal_system?: RefferalSystem;
  }
  