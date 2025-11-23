import React, { useEffect, useState } from 'react';

const Users = () => {
  const [data, setData] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  const fetchData = () => {
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Users endpoint:', endpoint);
        console.log('Fetched data:', results);
      })
      .catch(err => console.error('Error fetching users:', err));
  };

  useEffect(() => {
    fetchData();
  }, [endpoint]);

  return (
    <div className="container">
      <div className="card mb-4">
        <div className="card-body">
          <h2 className="card-title mb-4">Users</h2>
          <button className="btn btn-primary mb-3" onClick={fetchData}>Refresh</button>
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead className="table-dark">
                <tr>
                  <th>#</th>
                  <th>Username</th>
                  <th>Email</th>
                </tr>
              </thead>
              <tbody>
                {data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    <td>{item.id || idx + 1}</td>
                    <td>{item.username || '-'}</td>
                    <td>{item.email || '-'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Users;
