// Welcome to Secure Code Game Season-2/Level-5!

// This is the last level of this season, good luck!

const CryptoAPI = (function() {
    const encoding = {
        a2b: (a) => new TextEncoder().encode(a),
        b2a: (b) => new TextDecoder().decode(b),
    };

    const API = {
        sha256: {
            name: "sha256",
            identifier: "2b0e03021a",
            size: 32,
            async hash(s) {
                const encoder = new TextEncoder();
                const data = encoder.encode(s);
                const hashBuffer = await crypto.subtle.digest("SHA-256", data);
                return Array.from(new Uint8Array(hashBuffer))
                    .map((b) => b.toString(16).padStart(2, "0"))
                    .join("");
            }
        }
    };

    return API;
})();